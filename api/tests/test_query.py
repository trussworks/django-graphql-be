"""Tests for optimizing GraphQL queries"""
from typing import cast

import pytest
import sqlparse
from graphql.language import parser, ast, source
from graphene import ResolveInfo
from snapshottest.pytest import PyTestSnapshotTest
from django.db.models import sql

from api.query import GrapheneQueryMixin, ImplementationError
from api.models import Incident


def graphql_parser(gql_snippet: str) -> parser.Parser:
    """
    Return a parser object that can be used to create an Abstract Syntax Tree (AST) representation of the GQL snippet
    provided.
    """
    return parser.Parser(source.Source(gql_snippet), options={"no_location": False, "no_source": False})


class TestGrapheneQueryMixinArgs:
    """Test that `GrapheneQueryMixin` correctly identifies the select and/or prefetch args specified in the GQL query"""

    DEFAULT_GQL_SNIPPET = '''
      {
        id
        summary
        status
        colorCode
        subject {
          firstName
          lastName
          incidents {
            id
            summary
          }
        }
        analyst {
          firstName
          lastName
          incidents {
            summary
            status
          }
          incidentsAssigned {
            colorCode
          }
        }
        receivedAt
        createdAt
        updatedAt
      }
    '''

    def default_selections(self) -> list[ast.Field]:
        """Set up a default list of field selections for each test"""
        return cast(list[ast.Field], parser.parse_selection_set(graphql_parser(self.DEFAULT_GQL_SNIPPET)).selections)

    def test_find_query_args__empty(self) -> None:
        """Not specifying select/prefetch fields should not cause an error nor produce any query arguments"""
        class EmptyFields(GrapheneQueryMixin):
            """This model has not defined select or prefetch args"""

        select_args, prefetch_args = EmptyFields._find_query_args(self.default_selections())
        assert select_args == []
        assert prefetch_args == []

    def test_find_query_args__selected(self) -> None:
        """
        If fields that are specified on the model class are also selected in the GraphQL query,
        they should appear in the returned select/prefetch args.
        """
        class SelectedFields(GrapheneQueryMixin):
            """All of the fields here are in the default selection set and should thus all be in the resulting args"""

            select_fields = ("analyst", )
            prefetch_fields = ("subject__incidents", )

        select_args, prefetch_args = SelectedFields._find_query_args(self.default_selections())
        assert select_args == ["analyst"]
        assert prefetch_args == ["subject__incidents"]

    def test_find_query_args__non_selected(self) -> None:
        """
        If fields that are specified on the model class are NOT selected in the query, they should not be returned in
        the query args. This should also not be an error.
        """
        class NonSelectedFields(GrapheneQueryMixin):
            """These fields do not exist in the provided selection set, and so will not be returned"""

            select_fields = ("color", "weight")
            prefetch_fields = ("weight__units", )

        select_args, prefetch_args = NonSelectedFields._find_query_args(self.default_selections())
        assert select_args == []
        assert prefetch_args == []

    def test_find_query_args__only_prefetch(self) -> None:
        """Omitting either select or prefetch fields on the model class definition should not cause an error"""
        class OnlyPrefetchFields(GrapheneQueryMixin):
            """This mock model only defines prefetch fields"""

            prefetch_fields = ("cases", "subject__incidents", "subject__incidents_assigned")

        select_args, prefetch_args = OnlyPrefetchFields._find_query_args(self.default_selections())
        assert select_args == []
        # verify neither `incidents` nor `subject__incidents_assigned` were selected:
        assert prefetch_args == ["subject__incidents"]

    def test_find_query_args__prefixed(self) -> None:
        """Specifying a prefix should limit which fields are recognized as a query args"""
        class PrefixedFields(GrapheneQueryMixin):
            """All of these fields will be prefixed by the _find_query_args method"""

            select_fields = ("color_code", "status", "subject", "pre_status")
            prefetch_fields = ("analyst", "analyst__first_name", "pre_analyst__first_name")

        select_args, prefetch_args = PrefixedFields._find_query_args(self.default_selections(), "pre_")

        # Only the fields that were prefixed with "pre_" should be selected:
        assert select_args == ["pre_status"]
        assert prefetch_args == ["pre_analyst__first_name"]


class TestGrapheneQueryMixinSQL:
    """Test that the SQL generated by `GrapheneQueryMixin` matches expectations"""
    @staticmethod
    def mock_resolve_info(field_snippet: str) -> ResolveInfo:
        """
        Create and return a mocked version of the ResolveInfo class,
        which includes only the necessary attributes for the `build_optimized_query()` method.
        """
        class MockResolveInfo:
            field_asts = [parser.parse_field(graphql_parser(field_snippet))]

        return cast(ResolveInfo, MockResolveInfo())

    @staticmethod
    def pretty_print_sql(query: sql.Query) -> str:
        """Parse a QuerySet into a string of well-formatted SQL"""
        return sqlparse.format(str(query), reindent=True, keyword_case='upper')

    def test_case_query_simple(self, snapshot: PyTestSnapshotTest) -> None:
        """Test that a simple request results in a simple query"""
        mock_simple_cases_query = self.mock_resolve_info('''
          allIncidents {
            id
            summary
            status
            colorCode
          }
        ''')
        query = Incident.build_optimized_query(mock_simple_cases_query).all().query
        snapshot.assert_match(self.pretty_print_sql(query))

    def test_case_query_complex(self, snapshot: PyTestSnapshotTest) -> None:
        """Test that a complex request adds expected complexity to the query"""
        mock_complex_cases_query = self.mock_resolve_info('''
          allIncidents {
            id
            summary
            status
            colorCode
            subject {
              firstName
              lastName
              incidents {
                id
              }
            }
            analyst {
              firstName
              lastName
            }
          }
        ''')
        query = Incident.build_optimized_query(mock_complex_cases_query).all().query
        snapshot.assert_match(self.pretty_print_sql(query))

    def test_build_optimized_query__implementation_error(self) -> None:
        """
        Although `_find_query_args` works without being subclassed with a Django Model,
        `build_optimized_query` should fail.
        """
        class NonSubclasssedModel(GrapheneQueryMixin):
            """This class was not subclassed with a Model, and thus should fail"""

        mock_resolve_info = self.mock_resolve_info('''
          allIncidents {
            id
          }
        ''')
        with pytest.raises(ImplementationError):
            _ = NonSubclasssedModel.build_optimized_query(mock_resolve_info)
