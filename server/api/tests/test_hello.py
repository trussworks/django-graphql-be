import json

from django.test import TestCase
from graphene.test import Client
from graphene_django.utils.testing import GraphQLTestCase
from snapshottest.django import TestCase as SnapshotTestCase


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

        # This line checks a specific field
        assert content["data"]["hello"] == "Hello World!"

        # This line makes a snapshot the first time, then compares against the snapshot
        self.assertMatchSnapshot(response)
        self.assertMatchSnapshot(content)
