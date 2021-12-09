import os
import pprint
from typing import Any

from invoke import Context, UnexpectedExit, task, Config, tasks
from .common import server_path


@task
def mypy(c):
    # type: (Context) -> None
    """
    Runs the mypy typecheck on all python folders
    """
    c.run('mypy tasks')
    c.run('mypy server')

@task(help={"snapshot_update": "Updates testing snapshots if needed"})
def test(c, snapshot_update=False):
    # type: (Context, bool) -> None
    """
    Runs all tests available on the server
    """
    with c.cd(server_path()):
        c.run('python manage.py test')
