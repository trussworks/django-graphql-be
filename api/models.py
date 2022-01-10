"""Model definitions for DB schema"""
from django.db import models

from . import constants
from .query import GrapheneQueryMixin


class Person(GrapheneQueryMixin, models.Model):  # type: ignore[misc]
    first_name = models.CharField(max_length=80, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    # Set automatically when created/updated:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # GraphQL query fields:
    prefetch_fields = ("cases", "cases_assigned", "cases__analyst", "cases_assigned__subject")

    class Meta:
        verbose_name_plural = "people"

    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"


class Case(GrapheneQueryMixin, models.Model):  # type: ignore[misc]
    subject = models.ForeignKey(Person, related_name="cases", on_delete=models.PROTECT)
    analyst = models.ForeignKey(Person, related_name="cases_assigned", on_delete=models.SET_NULL, null=True, blank=True)
    summary = models.CharField(max_length=200, null=True, blank=True)
    color_code = models.CharField(max_length=6, choices=constants.COLOR_CODE_CHOICES, null=True, blank=True)
    status = models.CharField(max_length=20, choices=constants.STATUS_CHOICES, null=True, blank=True)
    received_at = models.DateTimeField(null=True)

    # Set automatically when created/updated:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # GraphQL query fields:
    select_fields = ("subject", "analyst")
    prefetch_fields = ("subject__cases", "subject__cases_assigned", "analyst__cases", "analyst__cases_assigned")

    def __str__(self) -> str:
        return f"{self.subject} - {self.summary if self.summary else '[N/A]'}"