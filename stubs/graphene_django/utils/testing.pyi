"""graphene-django testing utils"""
from typing import Union

from django.test import Client
from django.http import HttpResponse


def graphql_query(query: str, **kwargs: Union[str, dict, Client]) -> HttpResponse:
    """Definition: https://github.com/graphql-python/graphene-django/blob/main/graphene_django/utils/testing.py#L9"""
