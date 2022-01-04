import os
import time
from typing import cast

from invoke import task, UnexpectedExit, Context


class Database:

    def __init__(self, container: str, name: str, password: str, port: int, docker_port: int) -> None:
        self.container = container
        self.name = name
        self.password = password
        self.port = port
        self.docker_port = docker_port
        self.image = 'postgres:12.7'
        self.psql_cmd = '/usr/local/bin/psql --variable "ON_ERROR_STOP=1"'

    def conninfo(self, db: str = '') -> str:
        """
        Returns a connection info string to use with psql command.
        Defaults to no specific db, select db if needed
        """
        return f"postgres://postgres:{self.password}@localhost:{self.port}/{db}"

    def check(self, c: Context, db: str = '', retry: int = 3, sleep: int = 1) -> None:  #type: ignore[no-any-unimported]
        """
        Attempt to connect to the postgres instance.
        """

        for i in range(retry):
            try:
                c.run(f"{self.psql_cmd} {self.conninfo()} -c 'SELECT 1;'", hide=True)
            except UnexpectedExit:
                print("Could not connect to db, retrying...")
                time.sleep(sleep)
                if i < retry - 1:
                    continue
                else:
                    raise

            print("Success! Connected.")
            break

    def create(self, c: Context) -> None:  #type: ignore[no-any-unimported]
        """
        Create a database in the docker container
        """
        cmd = f"CREATE DATABASE {self.name};"
        print(cmd)
        c.run(f"{self.psql_cmd} {self.conninfo()} -c \"{cmd}\"")
        print(f"Success! Created database {self.name}")


# Database details to be used for these commands
db = Database(
    container='sith-dev-db',
    name=os.environ.get('DB_NAME', ''),
    password=os.environ.get('DB_PASSWORD', ''),
    port=cast(int, os.environ.get('DB_PORT')),
    docker_port=5432,
)


@task(default=True)
def start(c):  #type: ignore[no-any-unimported]
    # type: (Context) -> None
    """
    Restart (or create) the docker container with the database
    """
    print("Start the database container")
    result = None
    create_db = False
    try:
        c.run(f"docker start {db.container}")
        print(f"Success! Container {db.container} running")

    except UnexpectedExit:

        print("Unable to start container, create a new database container")
        result = c.run(
            f"docker run -d --name {db.container} -e POSTGRES_PASSWORD={db.password} -p {db.port}:{db.docker_port} {db.image}"
        )

        # ^^ c.run by default exits if a command fails
        print(f"Success! Container {db.container} running")
        create_db = True

    if create_db:
        try:
            db.check(c)
            db.create(c)
        except UnexpectedExit as e:
            print(f"Error executing: {e.result.command}")


@task(pre=[start])
def create(c):  #type: ignore[no-any-unimported]
    # type: (Context) -> None
    """
    Create the database in the docker container
    """
    try:
        db.check(c)
        db.create(c)
    except UnexpectedExit as e:
        print(f"Error executing: {e.result.command}")


@task()
def check(c):  #type: ignore[no-any-unimported]
    # type: (Context) -> None
    """
    Check that you can connect to the database in the docker container
    """
    print(f"Connecting to {db.name}")
    try:
        db.check(c, db=db.name)
    except UnexpectedExit as e:
        print(f"Error executing: {e.result.command}")


@task()
def destroy(c):  #type: ignore[no-any-unimported]
    # type: (Context) -> None
    """
    Destroy the database and the docker container
    """
    print(f"Destroying container {db.container}")
    c.run(f"docker rm -f {db.container}")
