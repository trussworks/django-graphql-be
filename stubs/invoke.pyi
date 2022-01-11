"""Stubs for the invoke module - https://docs.pyinvoke.org/en/stable/index.html"""
from typing import Union, Callable, Optional, mod
from types import ModuleType


class Collection:
    def add_collection(
            self,
            coll: Union[Collection, ModuleType],
            name: Optional[str] = None,
            default: Optional[bool] = None
    ) -> None:
        ...

class Result:
    command: str

class Failure(Exception):
    result: Result

class UnexpectedExit(Failure):  ...

class Context:
    def run(self, command: str, **kwargs: bool) -> None:
        """
        Run shell/terminal commands.
        The only `kwargs` used so far are bool, but this type can be expanded to a Union with more key word types.
        """

def task(*args: Union[Callable, list[Callable]], **kwargs: Union[bool, dict[str, str], list[Callable]]) -> Callable:
    """
    """
