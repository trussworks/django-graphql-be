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
