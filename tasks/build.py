from invoke import task, UnexpectedExit
from typing import Any


@task
def typecheck(c):
    # type: (Any) -> None
    """

    """
    c.run('mypy tasks')
    c.run('mypy server')
