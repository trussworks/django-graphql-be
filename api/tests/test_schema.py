"""Tests for the graphql API schema"""
import json

from django.http import HttpResponse
from snapshottest.pytest import PyTestSnapshotTest

from .conftest import PopulateDbType, ClientQueryType


def test_all_cases(populate_db: PopulateDbType, client_query: ClientQueryType, snapshot: PyTestSnapshotTest) -> None:
    """Test the resolver for returning all cases from DB"""

    # Load default test data into the database:
    populate_db()

    response: HttpResponse = client_query('''
        query {
          allCases {
            id
            subject {
              firstName
              lastName
            }
            analyst {
              firstName
              lastName
            }
            summary
            colorCode
            status
            receivedAt
          }
        }
        ''')
    assert response.status_code == 200, f"The response failed with a {response.status_code} status code."

    content: dict = json.loads(response.content)
    # This line makes a snapshot the first time, then compares against the snapshot
    snapshot.assert_match(content)


def test_all_people(populate_db: PopulateDbType, client_query: ClientQueryType, snapshot: PyTestSnapshotTest) -> None:
    """Test the resolver for returning all people (Person data) from DB"""

    # Load default test data into the database:
    populate_db()

    response: HttpResponse = client_query('''
        query {
          allPeople {
            id
            firstName
            lastName
            cases {
              summary
              colorCode
              status
              receivedAt
            }
            casesAssigned {
              summary
              colorCode
              status
              receivedAt
            }
          }
        }
        ''')
    assert response.status_code == 200, f"The response failed with a {response.status_code} status code."

    content: dict = json.loads(response.content)
    # This line makes a snapshot the first time, then compares against the snapshot
    snapshot.assert_match(content)
