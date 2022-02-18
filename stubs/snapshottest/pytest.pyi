"""Pytest-specific testing tools"""
from typing import Any

from pytest import FixtureRequest


class PyTestSnapshotTest:
    def __init__(self, request: FixtureRequest) -> None: ...

    def assert_match(self, value: Any, name: str = "") -> None:  #type: ignore[misc]
        """
        Check that a snapshot matches a provided value. `value` MUST be `Any` in this case because this function is
        designed to determine what type `value` is itself and then compare accordingly.

        The idea is truly that ANY value can have a snapshot.
        """
