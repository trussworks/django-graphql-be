import json

from graphene_django.utils.testing import GraphQLTestCase
from snapshottest.django import TestCase as SnapshotTestCase


class HelloTestCase(GraphQLTestCase, SnapshotTestCase):  #type: ignore[no-any-unimported]

    def test_hello(self) -> None:
        response = self.query('''
            query {
                hello
            }
            ''',)

        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)

        # This line checks a specific field
        assert content["data"]["hello"] == "Hello World!"

        # This line makes a snapshot the first time, then compares against the snapshot
        self.assertMatchSnapshot(response)
        self.assertMatchSnapshot(content)
