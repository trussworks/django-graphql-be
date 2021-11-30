# SITH Backend

The SITH backend is a django-based backend for the System for Insider Threat Hindrance (SITH) project

## Usage

### Install Python and Packages

This project is compatible with Python 3.9.

Create a virtualenv if you prefer (TBD Recommendation from project team)

Use the package manager `pip` to install the packages.

```sh
pip install -r requirements.txt
```

This project uses Invoke to aggregate all useful commands and scripts. Run invoke from the top level folder.

```sh
> inv -l
````

Read more about [invoke here](https://truss-dds.atlassian.net/wiki/spaces/eng/pages/50790405/Invoke).

### Install and Create Database

The database is a postgres container which runs inside a docker container.

First time running this project? Please run Docker and install postgres.

```sh
brew install postgres
```

Create and run the database using invoke

```sh
inv db.start
```

### Run the Backend

Run the server

```sh
cd sith_django
python manage.py runserver
```

You should be able to access the graphql browser at `http://127.0.0.1:8000/graphql`

The graphql query:

```graphql
query {
  hello
}
```

should respond with:

```json
{
  "data": {
    "hello": "Hello World!"
  }
}
```

## Typechecking

To typecheck the project, from the toplevel call

```sh
inv build.mypy
```

You should see no errors.

```sh
Success: no issues found in 3 source files
Success: no issues found in 14 source files
```
