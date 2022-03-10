"""Tests for DB models"""
from datetime import datetime

import pytest
from django.db.models import ProtectedError
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

from api.models import Person, Incident
from api.constants import COLOR_CODE_CHOICES


@pytest.mark.django_db
class TestModelPerson:

    @pytest.mark.parametrize(
        ("first_name", "last_name"),
        [
            ("Test", "Testing"),
            ("No last name", ""),
            ("", "No first name"),
            ("", ""),
        ],
    )
    def test_str(self, first_name: str, last_name: str) -> None:
        """Test that the string representation of a Person is what we expect"""

        # NOTE: This does NOT save a Person on the database.
        # We just need an instance of the class to test its string representation.
        person = Person(first_name=first_name, last_name=last_name)

        assert str(person) == f"{last_name}, {first_name}"

    def test_create(self) -> None:
        """Test that a Person record can be successfully created on the DB"""
        person = Person()
        person.save()  # this line commits the model record to the database

        assert person.pk is not None
        assert person.created_at is not None
        assert person.updated_at is not None

    def test_update(self) -> None:
        """Test that an existing Person record can be updated in the DB"""
        person = Person()
        person.save()
        initial_created_at = person.created_at
        initial_updated_at = person.updated_at

        test_first_name = "Test"
        person.first_name = test_first_name
        person.save()  # `save()` is used to perform creates AND updates

        assert person.pk is not None
        assert person.first_name == test_first_name
        assert person.created_at == initial_created_at
        assert person.updated_at > initial_updated_at


@pytest.mark.django_db
class TestModelIncident:

    def test_str(self) -> None:
        """Test that the string representation of an Incident is what we expect"""
        incident = Incident(subject=self.create_subject(commit=False))
        assert str(incident) == f"{incident.subject} - [N/A]"

        incident.summary = "test summary"
        assert str(incident) == f"{incident.subject} - {incident.summary}"

    def test_create_no_subject_failure(self) -> None:
        """An incident should require a Person subject to be associated with it, so a create should fail without one"""
        incident = Incident()

        with pytest.raises(IntegrityError) as e:
            incident.save()

        # Check that the subject_id column did indeed cause the error
        assert "subject_id" in str(e.value)

    def test_choice_failure(self) -> None:
        """Test that updating a `color_code` or `status` to an option not in the choices FAILS"""
        fake_color_code = "fake"
        assert not any(fake_color_code in choice for choice in COLOR_CODE_CHOICES)

        incident = Incident(subject=self.create_subject(), received_at=datetime.now(), color_code=fake_color_code)

        with pytest.raises(ValidationError) as e:
            # this is the method that validates Django models, `save()` does not do this by default:
            incident.full_clean()

        # Verify that the field we were testing is indeed one of the errors
        assert "color_code" in e.value.error_dict

    def test_delete_analyst(self) -> None:
        """
        Test deleting the Person record for an `analyst` to see that the field becomes NULL on the Incident record
        """
        analyst = Person(first_name="Test", last_name="Analyst")
        analyst.save()
        assert analyst.pk is not None

        # Create an incident record
        incident = Incident(subject=self.create_subject(), analyst=analyst)
        incident.save()
        assert incident.pk is not None

        # Delete the analyst for the incident
        analyst.delete()

        # Re-retrieve the incident from the DB
        incident = Incident.objects.get(pk=incident.pk)
        assert incident.analyst is None

    def test_delete_subject_failure(self) -> None:
        """
        Test attempting to delete a Person record for a `subject` and verify that we receive an error
        """
        subject = self.create_subject()
        incident = Incident(subject=subject)
        incident.save()
        assert incident.pk is not None

        # Try to delete the subject of the incident, but expect an error from the database
        with pytest.raises(ProtectedError):
            subject.delete()  # no assertion, the above catch is the assertion

    @staticmethod
    def create_subject(commit: bool = True) -> Person:
        """Create a subject for an incident record"""
        subject = Person(first_name="Test", last_name="Incident Subject")
        if commit:
            subject.save()
            assert subject.pk is not None
        return subject
