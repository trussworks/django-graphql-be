# api/schema.py
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

    @staticmethod
    def resolve_all_cases(root: Optional[type], info: graphene.ResolveInfo) -> QuerySet:
        return Case.objects.select_related("subject", "analyst").all()


schema = graphene.Schema(query=Query)
