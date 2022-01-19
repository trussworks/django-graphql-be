"""Tasks to build and test the server"""
from invoke import Context, task, exceptions
import logging

log = logging.getLogger(__name__)


@task
def mypy(c):  # type: ignore[no-any-unimported]
    # type: (Context) -> None  # ignores Context type
    """
    Runs the mypy type check on all python folders
    """
    for mypy_dir in ['tasks', 'server', 'api']:
        log.info(f"Checking {mypy_dir}...")
        try:
            c.run(f'mypy {mypy_dir}')
        except exceptions.Failure:
            log.info(f"Errors found in {mypy_dir}.\n")


@task(help={"snapshot_update": "Updates testing snapshots if needed"})
def test(c, snapshot_update=False):  # type: ignore[no-any-unimported]
    # type: (Context, bool) -> None  # ignores Context type
    """
    Runs all tests available on the server
    """
    if snapshot_update:
        log.info("Updating snapshots...")
    # Run tests (with flags if necessary)
    c.run(f'pytest{" --snapshot-update" if snapshot_update else ""}')


@task
def format_code(c):  # type: ignore[no-any-unimported]
    # type: (Context) -> None  # ignores Context type
    """
    Formats the code using yapf
    """
    log.info("Formatting code...")
    c.run('yapf --in-place --recursive --parallel .')
    log.info('Formatting complete')


@task(pre=[mypy, format_code])
def tidy(c):  # type: ignore[no-any-unimported]
    # type: (Context) -> None  # ignores Context type
    """
    Runs all formatters, linters and static code analysis
    Most are run as prerequisites.
    """
    log.info("Build tidy completed")
