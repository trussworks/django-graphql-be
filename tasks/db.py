from invoke import task, UnexpectedExit  # type:ignore
import time


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
        return 'postgres://postgres:{pwd}@localhost:{port}/{db}'.format(
            pwd=self.password,
            port=self.port,
            db=db
        )

    def check(self, c, db: str = '', retry: int = 3, sleep: int = 1) -> None:
        """
        Attempt to connect to the postgres instance.
        """

        for i in range(retry):
            try:
                c.run('{psql} {conn} -c {cmd}'.format(
                    psql=self.psql_cmd,
                    conn=self.conninfo(),
                    cmd='SELECT 1;'
                ), hide=True)
            except UnexpectedExit as e:
                print("Could not connect to db, retrying...")
                time.sleep(sleep)
                if i < retry - 1:
                    continue
                else:
                    raise

            print("Success! Connected.")
            break

    def create(self, c) -> None:
        """
        Create a database in the docker container
        """
        cmd = 'CREATE DATABASE {};'.format(self.name)
        print(cmd)
        c.run('{psql} {conn} -c "{cmd}"'.format(
            psql=self.psql_cmd,
            conn=self.conninfo(),
            cmd=cmd
        ))
        print("Success! Created database {}".format(self.name))


# Database details to be used for these commands
db = Database(
    container='sith-dev-db',
    name='dev_db',
    password='dreampony',
    port=5433,
    docker_port=5432,
)


@task
def start(c) -> None:
    """
    Restart (or create) the docker container with the database
    """
    print("Start the database container")
    result = None
    try:
        if c.run('docker start {dckr}'.format(dckr=db.container)):
            print("Success! Container {} running".format(db.container))

    except UnexpectedExit:

        print("Unable to start container, create a new database container")
        result = c.run('docker run -d --name {dckr} -e POSTGRES_PASSWORD={pwd} -p {pext}:{pint} {pver}'
                       .format(
                           dckr=db.container,
                           pwd=db.password,
                           pext=db.port,
                           pint=db.docker_port,
                           pver=db.image
                       ))
        if result.return_code == 0:
            print("Success! Container {} running".format(db.container))


@task(pre=[start])
def create(c) -> None:
    """
    Create the database in the docker container
    """
    try:
        db.check(c)
        db.create(c)
    except UnexpectedExit as e:
        print("Error executing: {}".format(e.result.command))
        # c.run('echo yes')


@task()
def check(c) -> None:
    """
    Check that you can connect to the database in the docker container
    """
    print("Connecting to {}".format(db.name))
    try:
        db.check(c, db=db.name)
    except UnexpectedExit as e:
        print("Error executing: {}".format(e.result.command))


@task()
def destroy(c) -> None:
    """
    Destroy the database and the docker container
    """
    print("Destroying container {}".format(db.container))
    c.run('docker rm -f {}'.format(db.container))
