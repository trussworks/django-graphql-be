"""GraphQL API schema definition"""
from typing import Optional

import graphene
from graphene_django import DjangoObjectType
from django.db.models import QuerySet

from .models import Person, Incident


class PersonType(DjangoObjectType):

    class Meta:
        model = Person
        description = "The Person resource contains information about people such as the subject of an incident report"


class IncidentType(DjangoObjectType):

    class Meta:
        model = Incident
        description = "The Incident contains information about a specific incident and case. It is usually associated with a subject Person"


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello World!", description="Returns a Hello World! string")
    all_incidents = graphene.List(IncidentType, description="Returns a list of Incidents")
    all_people = graphene.List(PersonType, description="Returns a list of Person entries")

    class Meta:
        description = "Queries in GraphQl request information from the server"

    @staticmethod
    def resolve_all_incidents(root: Optional[type], info: graphene.ResolveInfo) -> QuerySet:
        return Incident.build_optimized_query(info).all()

    @staticmethod
    def resolve_all_people(root: Optional[type], info: graphene.ResolveInfo) -> QuerySet:
        return Person.build_optimized_query(info).all()


schema = graphene.Schema(query=Query)
