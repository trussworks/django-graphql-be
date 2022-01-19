import logging
import os
import time
from typing import cast

from invoke import Context, UnexpectedExit, task

log = logging.getLogger(__name__)


class Database:
    def __init__(self, container: str, name: str, password: str, port: int, docker_port: int) -> None:
        self.container = container
        self.name = name
        self.password = password
        self.port = port
        self.docker_port = docker_port
        self.image = 'postgres:12.7'
        self.psql_cmd = '/usr/local/bin/psql --variable "ON_ERROR_STOP=1"'

    def conninfo(self, db_name: str = '') -> str:
        """
        Returns a connection info string to use with psql command.
        Defaults to no specific db, select db if needed
        """
        return f"postgres://postgres:{self.password}@localhost:{self.port}/{db_name}"

    def check(self, c: Context, db_name: str = '', retry: int = 3, sleep: int = 1) -> None:
        """Attempt to connect to the postgres instance"""

        for i in range(retry):
            try:
                c.run(f"{self.psql_cmd} {self.conninfo(db_name)} -c 'SELECT 1;'", hide=True)
            except UnexpectedExit:
                log.warning("Could not connect to db, retrying...")
                time.sleep(sleep)
                if i < retry - 1:
                    continue
                else:
                    raise

            log.info("Success! Connected.")
            break

    def create(self, c: Context) -> None:
        """Create a database in the docker container"""
        cmd = f"CREATE DATABASE {self.name};"
        log.info(cmd)
        c.run(f"{self.psql_cmd} {self.conninfo()} -c \"{cmd}\"")
        log.info(f"Success! Created database {self.name}")


# Database details to be used for these commands
db = Database(
    container='sith-dev-db',
    name=os.environ.get('DB_NAME', ''),
    password=os.environ.get('DB_PASSWORD', ''),
    port=cast(int, os.environ.get('DB_PORT')),
    docker_port=5432,
)


@task(default=True)
def start(c):
    # type: (Context) -> None
    """
    Restart (or create) the docker container with the database
    """
    log.info("Start the database container")
    create_db = False
    try:
        c.run(f"docker start {db.container}")
        log.info(f"Success! Container {db.container} running")

    except UnexpectedExit:

        log.error("Unable to start container, create a new database container")
        c.run(f"docker run -d --name {db.container} -e POSTGRES_PASSWORD={db.password} -p {db.port}:{db.docker_port} "
              f"{db.image}")

        # ^^ c.run by default exits if a command fails
        log.info(f"Success! Container {db.container} running")
        create_db = True

    if create_db:
        try:
            db.check(c)
            db.create(c)
        except UnexpectedExit as e:
            log.exception(f"Error executing: {e.result.command}")


@task(pre=[start])
def create(c):
    # type: (Context) -> None
    """
    Create the database in the docker container
    """
    try:
        db.check(c)
        db.create(c)
    except UnexpectedExit as e:
        log.exception(f"Error executing: {e.result.command}")


@task
def check(c):
    # type: (Context) -> None
    """
    Check that you can connect to the database in the docker container
    """
    log.info(f"Connecting to {db.name}")
    try:
        db.check(c, db_name=db.name)
    except UnexpectedExit as e:
        log.error(f"Error executing: {e.result.command}")


@task
def destroy(c):
    # type: (Context) -> None
    """
    Destroy the database and the docker container
    """
    log.info(f"Destroying container {db.container}")
    c.run(f"docker rm -f {db.container}")
