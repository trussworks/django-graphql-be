import json

from django.test import TestCase
from graphene.test import Client
from graphene_django.utils.testing import GraphQLTestCase
from snapshottest import TestCase as SnapshotTestCase


class HelloTestCase(GraphQLTestCase, SnapshotTestCase):

    def test_hello(self):
        response = self.query('''
            query {
                hello
            }
            ''',)

        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)

        # Add some more asserts if you like
        assert content["data"]["hello"] == "Hello World!"
        self.assertMatchSnapshot(content)
