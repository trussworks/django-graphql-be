"""Model definitions for DB schema"""
from django.db import models

from . import constants
from .query import GrapheneQueryMixin


class Person(GrapheneQueryMixin, models.Model):  # type: ignore[misc]
    first_name = models.CharField(max_length=80, null=True, blank=True, help_text="First name of Person")
    last_name = models.CharField(max_length=100, null=True, blank=True, help_text="Last name of Person")

    # Set automatically when created/updated:
    created_at = models.DateTimeField(auto_now_add=True, help_text="Time at which entry was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Time at which entry was last updated")

    # GraphQL query fields:
    prefetch_fields = ("incidents", "incidents_assigned", "incidents__analyst", "incidents_assigned__subject")

    class Meta:
        verbose_name_plural = "people"

    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"


class Incident(GrapheneQueryMixin, models.Model):  # type: ignore[misc]
    subject = models.ForeignKey(Person,
                                related_name="incidents",
                                on_delete=models.PROTECT,
                                help_text="Subject of the incident")
    analyst = models.ForeignKey(Person,
                                related_name="incidents_assigned",
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                help_text="Analyst assigned to the incident")
    summary = models.CharField(max_length=200, null=True, blank=True, help_text="Quick summary of the incident")
    color_code = models.CharField(max_length=6,
                                  choices=constants.COLOR_CODE_CHOICES,
                                  null=True,
                                  blank=True,
                                  help_text="Color code of the label")
    status = models.CharField(max_length=20,
                              choices=constants.STATUS_CHOICES,
                              null=True,
                              blank=True,
                              help_text="Status of the incident")
    received_at = models.DateTimeField(null=True, help_text="Time at which incident information was received")

    # Set automatically when created/updated:
    created_at = models.DateTimeField(auto_now_add=True, help_text="Time at which incident was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Time at which incident was last updated")

    # GraphQL query fields:
    select_fields = ("subject", "analyst")
    prefetch_fields = ("subject__incidents", "subject__incidents_assigned", "analyst__incidents",
                       "analyst__incidents_assigned")

    def __str__(self) -> str:
        return f"{self.subject} - {self.summary if self.summary else '[N/A]'}"
