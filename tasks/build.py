"""Tasks to build and test the server"""
from invoke import Context, task


@task
def mypy(c): #type: ignore[no-any-unimported]
    # type: (Context) -> None
    """
    Runs the mypy typecheck on all python folders
    """
    c.run('mypy tasks')
    c.run('mypy server')

@task(help={"snapshot_update": "Updates testing snapshots if needed"})
def test(c, snapshot_update=False):  # type: ignore[no-any-unimported]
    # type: (Context, bool) -> None  # ignores Context type
    """
    Runs all tests available on the server
    """
    if snapshot_update:
        print("Updating snapshots...")
    c.run(f'pytest server{" --snapshot-update" if snapshot_update else ""}')
