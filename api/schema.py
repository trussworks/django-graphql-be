"""GraphQL API schema definition"""
from typing import Optional

import graphene
from graphene_django import DjangoObjectType
from django.db.models import QuerySet

from .query import DjangoQueryMixin
from .models import Person, Case


class PersonType(DjangoObjectType):  # type: ignore[no-any-unimported]
    class Meta:
        model = Person

    prefetch_fields = ("cases", "cases_assigned", "cases__analyst", "cases_assigned__subject")


class CaseType(DjangoObjectType):  # type: ignore[no-any-unimported]
    class Meta:
        model = Case

    select_fields = ("subject", "analyst")
    prefetch_fields = ("subject__cases", "subject__cases_assigned", "analyst__cases", "analyst__cases_assigned")


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello World!")
    all_cases = graphene.List(CaseType)
    all_people = graphene.List(PersonType)

    @staticmethod
    def resolve_all_cases(root: Optional[type], info: graphene.ResolveInfo) -> QuerySet:
        return Case.build_optimized_query(info).all()

    @staticmethod
    def resolve_all_people(root: Optional[type], info: graphene.ResolveInfo) -> QuerySet:
        return Person.build_optimized_query(info).all()


schema = graphene.Schema(query=Query)
