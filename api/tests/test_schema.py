"""Tests for the graphql API schema"""
import json

from django.http import HttpResponse
from django.core.management import call_command
from snapshottest.pytest import PyTestSnapshotTest

from .conftest import ClientQueryType, API_TESTS_DATA_DIR


def test_all_cases(db: None, client_query: ClientQueryType, snapshot: PyTestSnapshotTest) -> None:
    """Test the resolver for returning all cases from DB"""

    # Load test data into the database:
    call_command('loaddata', f'{API_TESTS_DATA_DIR}test_data.json')

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
