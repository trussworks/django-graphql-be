"""Utilities to improve query efficiency with Django + GraphQL"""
from typing import cast

from stringcase import snakecase
from graphql.language.ast import Field, SelectionSet
import graphene
from django.db.models import QuerySet


class GrapheneQueryMixin:
    """Add query optimization to `django.db.models.Model` class using the GraphQL resolver and Django base ORM"""

    select_fields: tuple[str, ...] = ()  # field arguments for a `select_related()` method call
    prefetch_fields: tuple[str, ...] = ()  # field arguments for a `prefetch_related()` method call

    @classmethod
    def build_optimized_query(cls, info: graphene.ResolveInfo) -> QuerySet:
        """Build an optimized QuerySet to be executed in a GraphQL query resolver.

        :param info:
            The Graphene object type that contains all pertinent information about the requested query.
        :return:
            A QuerySet that has been optimized but not resolved. Must be called with `.all()` or `.filter(...)` once
            returned.
        """
        # `cls` here IS the model type, so this is the typical `Model.objects` syntax.
        query = cls.objects  # type: ignore[attr-defined]

        # `info.field_asts[0]` is our API query name.
        # We need this to know that a query has even been requested - without it, we would have no idea what the client
        # wants from us.
        # We will let the IndexError/AttributeError raise if it doesn't exist because that would be extremely peculiar.
        select_args, prefetch_args = \
            cls._find_query_args(cast(SelectionSet, info.field_asts[0].selection_set).selections)

        if select_args:
            query = query.select_related(*select_args)

        if prefetch_args:
            query = query.prefetch_related(*prefetch_args)

        return cast(QuerySet, query)

    @classmethod
    def _find_query_args(cls, fields: list[Field], field_prefix: str = "") -> tuple[list[str], list[str]]:
        """Find arguments needed to optimize a query for the requested fields.

        :param fields:
            A list of `graphql.Field` objects that contain the information for each field requested.
        :param field_prefix:
            A string prefix that is added onto each requested field name before searching for the field in
            `cls.select_fields` or `cls.prefetch_fields`. Demonstrates relationships between related Django models.
        :return:
            A tuple with two lists. The first contains all arguments that should be passed into a `select_related`
            method on a QuerySet. The second contains all `prefetch_related` args.
        """
        select_args: list[str] = []
        prefetch_args: list[str] = []

        if not cls.select_fields and not cls.prefetch_fields:
            return select_args, prefetch_args

        for field in fields:
            field_name = f"{field_prefix}{snakecase(field.name.value)}"

            if field_name in cls.select_fields:
                select_args.append(field_name)

            if field_name in cls.prefetch_fields:
                prefetch_args.append(field_name)

            # If this field is itself an object type, search through its subfields for more query arguments:
            if field.selection_set:
                s, p = cls._find_query_args(field.selection_set.selections, f"{field_name}__")  # Django relation syntax
                select_args.extend(s)
                prefetch_args.extend(p)

        return select_args, prefetch_args
