"""
Define data and other config elements for tests.
`conftest.py` is a pytest standard file.
"""
from os import path
from typing import Union, Protocol

import pytest
from django.test.client import Client
from django.http import HttpResponse
from django.core.management import call_command
from snapshottest.pytest import PyTestSnapshotTest
from graphene_django.utils.testing import graphql_query

API_TESTS_DIR: str = path.dirname(__file__)
API_TESTS_DATA_DIR: str = path.join(API_TESTS_DIR, 'data/')

PopulateDbType = Callable[[str], None]

# typing.ParamSpec would be a compelling alternative to Union here (and TypeVar elsewhere),
# but it is only available in Python >=3.10
ClientQueryParams = Union[str, dict, Client]


class ClientQueryType(Protocol):
    def __call__(self, query: str, **kwargs: ClientQueryParams) -> HttpResponse:
        ...


@pytest.fixture
def populate_db(db: None) -> PopulateDbType:
    """
    Populate the DB with the data for a specific scenario/fixture.
    Can be used along with `@pytest.mark.django_db` to specify transaction settings and more
    (https://pytest-django.readthedocs.io/en/latest/database.html).

    :param db:
        `pytest-django`'s fixture to allow database access during tests.
        Source: https://github.com/pytest-dev/pytest-django/blob/master/pytest_django/fixtures.py#L302-L316
    :return:
        A callable that can be used to specify which fixture gets loaded for the test. Useful for testing scenarios.
    """
    def load_fixture(scenario: str = "default") -> None:
        call_command("loaddata", f"{API_TESTS_DATA_DIR}{scenario}.json")

    yield load_fixture


@pytest.fixture
def client_query(client: Client) -> ClientQueryType:
    """Use the Django `client` fixture with graphql_query"""
    def func(query: str, **kwargs: ClientQueryParams) -> HttpResponse:
        return graphql_query(query, **kwargs, client=client)

    return func


@pytest.fixture(scope="class")
def snapshot_pytest(request: pytest.FixtureRequest) -> None:
    """
    Wrap snapshot fixture to provide instance snapshot property for unittest.TestCase tests.
    `request` is a pytest fixture containing information about the test command:
    https://docs.pytest.org/en/latest/reference/reference.html#std-fixture-request
    """
    request.cls.snapshot = PyTestSnapshotTest(request)
