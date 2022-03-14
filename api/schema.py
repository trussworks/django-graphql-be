"""GraphQL API schema definition"""
from typing import Optional

import graphene
from graphene_django import DjangoObjectType
from django.db.models import QuerySet

from .models import Person, Incident


class PersonType(DjangoObjectType):

    class Meta:
        model = Person


class IncidentType(DjangoObjectType):

    class Meta:
        model = Incident


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello World!")
    all_incidents = graphene.List(IncidentType)
    all_people = graphene.List(PersonType)

    @staticmethod
    def resolve_all_incidents(root: Optional[type], info: graphene.ResolveInfo) -> QuerySet:
        return Incident.build_optimized_query(info).all()

    @staticmethod
    def resolve_all_people(root: Optional[type], info: graphene.ResolveInfo) -> QuerySet:
        return Person.build_optimized_query(info).all()


schema = graphene.Schema(query=Query)
