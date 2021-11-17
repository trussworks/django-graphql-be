# SITH Backend

The SITH backend is a django-based backend for the System for Insider Threat Hindrance (SITH) project

## Usage

This project is compatible with Python 3.9.

Create a virtualenv if you prefer (TBD Recommendation from project team)

Use the package manager `pip` to install the packages.

```
pip install -r requirements.txt
```

Run the server

```
cd sith_django
python manage.py runserver
```

You should be able to access the graphql browser at `http://127.0.0.1:8000/graphql`

The graphql query

```
query {
  hello
}
```

should respond with

```
{
  "data": {
    "hello": "Hello World!"
  }
}
```

## Typechecking

To typecheck the project, from the toplevel call

```
mypy sith_django
```

You should see only one error for the one module we haven't stubbed yet.

```
sith_django/app/urls.py:18: error: Skipping analyzing "graphene_django.views": found module but no type hints or library stubs
sith_django/app/urls.py:18: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
Found 1 error in 1 file (checked 14 source files)
```
