"""Tasks to build and test the server"""
from invoke import Context, task, exceptions


@task
def mypy(c):  # type: ignore[no-any-unimported]
    # type: (Context) -> None  # ignores Context type
    """
    Runs the mypy type check on all python folders
    """
    for mypy_dir in ['tasks', 'server']:
        print(f"Checking {mypy_dir}...")
        try:
            c.run(f'mypy {mypy_dir}')
        except exceptions.Failure:
            print(f"Errors found in {mypy_dir}.\n")


@task(help={"snapshot_update": "Updates testing snapshots if needed"})
def test(c, snapshot_update=False):  # type: ignore[no-any-unimported]
    # type: (Context, bool) -> None  # ignores Context type
    """
    Runs all tests available on the server
    """
    if snapshot_update:
        print("Updating snapshots...")
    c.run(f'pytest server{" --snapshot-update" if snapshot_update else ""}')
