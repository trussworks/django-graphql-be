"""
Define fixtures and other config elements for tests.
`conftest.py` is a pytest standard file.
"""
from os import path
from typing import Callable, Union, cast

import pytest
from _pytest.fixtures import FixtureRequest
from django.test.client import Client
from django.http import HttpResponse
from snapshottest.pytest import PyTestSnapshotTest
from graphene_django.utils.testing import graphql_query

API_TESTS_DIR: str = path.dirname(__file__)
API_TESTS_DATA_DIR: str = path.join(API_TESTS_DIR, 'data/')

# typing.ParamSpec would be a compelling alternative to Union here (and TypeVar elsewhere),
# but it is only available in Python >=3.10
ClientQueryParams = Union[str, dict]
ClientQueryType = Callable[[ClientQueryParams], HttpResponse]


@pytest.fixture
def client_query(client: Client) -> ClientQueryType:
    """Use the Django `client` fixture with graphql_query"""
    def func(*args: ClientQueryParams, **kwargs: ClientQueryParams) -> HttpResponse:
        return cast(HttpResponse, graphql_query(*args, **kwargs, client=client))

    return func


@pytest.fixture(scope="class")
def snapshot_pytest(request: FixtureRequest) -> None:
    """
    Wrap snapshot fixture to provide instance snapshot property for unittest.TestCase tests.
    `request` is a pytest fixture containing information about the test command:
    https://docs.pytest.org/en/latest/reference/reference.html#std-fixture-request
    """
    request.cls.snapshot = PyTestSnapshotTest(request)
