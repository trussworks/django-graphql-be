from invoke import task, UnexpectedExit
from typing import Any


@task
def mypy(c):
    # type: (Any) -> None
    """
    Runs the mypy typecheck on all python folders
    """
    c.run('mypy tasks')
    c.run('mypy server')
