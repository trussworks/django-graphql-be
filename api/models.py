from django.db import models

from . import constants


class Person(models.Model):
    first_name = models.CharField(max_length=80, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    # Set automatically when created/updated:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "people"

    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"


class Case(models.Model):
    subject = models.ForeignKey(Person, related_name="cases", on_delete=models.PROTECT)
    analyst = models.ForeignKey(Person, related_name="cases_assigned", on_delete=models.SET_NULL, null=True, blank=True)
    summary = models.CharField(max_length=200, null=True, blank=True)
    color_code = models.CharField(max_length=6, choices=constants.COLOR_CODE_CHOICES, null=True, blank=True)
    status = models.CharField(max_length=20, choices=constants.STATUS_CHOICES, null=True, blank=True)
    received_at = models.DateTimeField()

    # Set automatically when created/updated:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
