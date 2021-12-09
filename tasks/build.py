from invoke import task, UnexpectedExit, Context
from typing import Any


@task
def mypy(c):
    # type: (Context) -> None
    """
    Runs the mypy typecheck on all python folders
    """
    c.run('mypy tasks')
    c.run('mypy server')
