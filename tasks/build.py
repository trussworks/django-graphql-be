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

@task
def test(c):
    # type: (Context) -> None
    """
    Runs all tests available on the server
    """
    with c.cd('server/'):
        c.run('python manage.py test')


@task
def snapshot_update(c):
    # type: (Context) -> None
    """
    Runs all tests and overwrites snapshots for all snapshot tests
    """
    with c.cd('server/'):
        c.run('python manage.py test --snapshot-update')