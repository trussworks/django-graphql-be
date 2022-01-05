"""GraphQL API schema definition"""
from typing import Optional

import graphene
from graphene_django import DjangoObjectType
from django.db.models import QuerySet

from .models import Person, Case


class PersonType(DjangoObjectType):  # type: ignore[no-any-unimported]
    class Meta:
        model = Person


class CaseType(DjangoObjectType):  # type: ignore[no-any-unimported]
    class Meta:
        model = Case


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
