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
        select_args: list[str] = []
        prefetch_args: list[str] = []
        q = Case.objects

        # info.field_asts[0] is our API query name - we would not be here if we didn't have that
        for field in info.field_asts[0].selection_set.selections:
            if field.name.value in ["subject", "analyst"]:
                select_args.append(str(field.name.value))

                if field.selection_set and \
                        any(subfield.name.value.startswith("cases") for subfield in field.selection_set.selections):
                    prefetch_args.extend([f"{field.name.value}__cases", f"{field.name.value}__cases_assigned"])

        if any(select_args):
            q = q.select_related(*select_args)

            if any(prefetch_args):
                q = q.prefetch_related(*prefetch_args)

        return q.all()


schema = graphene.Schema(query=Query)
