"""Tasks to build and test the server"""
from invoke import Context, task, Failure


@task
def mypy(c):
    # type: (Context) -> None
    """
    Runs the mypy type check on all python folders
    """
    for mypy_dir in ['tasks', 'server', 'api']:
        print(f"Checking {mypy_dir}...")
        try:
            c.run(f'mypy {mypy_dir}')
        except Failure:
            print(f"Errors found in {mypy_dir}.\n")


@task(help={"snapshot_update": "Updates testing snapshots if needed"})
def test(c, snapshot_update=False):
    # type: (Context, bool) -> None
    """
    Runs all tests available on the server
    """
    if snapshot_update:
        print("Updating snapshots...")
    # Run tests (with flags if necessary)
    c.run(f'pytest{" --snapshot-update" if snapshot_update else ""}')


@task
def format_code(c):
    # type: (Context) -> None
    """
    Formats the code using yapf
    """
    print("Formatting code...")
    c.run('yapf --in-place --recursive --parallel .')
    print('Formatting complete')


@task(pre=[mypy, format_code])
def tidy(c):
    # type: (Context) -> None
    """
    Runs all formatters, linters and static code analysis
    Most are run as prerequisites.
    """
    print("Build tidy completed")
