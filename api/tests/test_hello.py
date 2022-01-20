import json

from django.http import HttpResponse
from snapshottest.pytest import PyTestSnapshotTest

from .conftest import ClientQueryType


class TestHello:
    def test_hello(self, client_query: ClientQueryType, snapshot: PyTestSnapshotTest) -> None:
        """Test the hello query in the GraphQL schema/API definition"""
        response: HttpResponse = client_query('''
            query {
                hello
            }
            ''')
        assert response.status_code == 200, f"The response failed with a {response.status_code} status code."

        content: dict = json.loads(response.content)
        # This line makes a snapshot the first time, then compares against the snapshot
        snapshot.assert_match(content)
