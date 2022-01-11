"""Stubs for the sqlparse module - https://sqlparse.readthedocs.io/en/latest/"""
from typing import Union, Optional, Protocol


def format(sql: str, encoding: Optional[str] = None, **kwargs: Union[bool, str, int]) -> str:  ...
