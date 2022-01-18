# BE-006 Datastore is a PostgreSQL db

**Status:** Accepted

**Drivers:** Shimona Carvalho

**Deciders:** Sandy Wright, Lindsay Techel, Patrick Dickey

**Decision Date:** 11/10/2021

## Context

We need an underlying datastore for our application. We have settled on a django backend and graphql API. It will need to be compatible with those choices.

## Decision

### Decision is to use a PostgreSQL database.

It’s one of the most powerful relational databases and the one that is most frequently used in conjunction with Django. Since Django only officially supports a shortlist of relational databases, all other styles of DB come with the risk of less robust third party libraries, and possible performance issues.

## Consequences

We’ll be able to move forward on our backend with a robust, well supported datastore.

## Options Considered

### PostgreSQL

PostgreSQL is the most widely used RDBMS databse with a django server. It is a relational database.

- `+` Very widely used, especially with django
- `+` A lot of team experience
- `+` Solid, robust, stable ORM in django
- `+` Django officially supports only RDBMS databases.
- `+` Django’s fast performance depends on a number of things including optimizing queries. It’s fair to assume it’s been designed to perform best with relational databases, since those are what is officially supported.
- `-` Not sure if graphQL lends itself more to a noSQL database?

### MongoDB

MongoDB is a document database.

- `-` Officially django only supports RDBMS
- `-` Packages available but many [articles](https://daniel.feldroy.com/posts/when-to-use-mongodb-with-django) discuss mongoDB not being a good fit with django
- `-` Lack of enforcement for types and structure can lead to graphQL errors

### Elasticsearch

Elasticsearch is a search and analytics engine

- `-` While elasticsearch can be used in conjunction with django, it’s not meant to be used as the underlying datastore.

### GraphDB

- `-` Lack of a robust, stable ORM for django
- `-` Officially django only supports RDBMS

## Resources

- [When to Use MongoDB with Django](https://daniel.feldroy.com/posts/when-to-use-mongodb-with-django)
- [Performance and optimization | Django documentation | Django](https://docs.djangoproject.com/en/3.2/topics/performance/)
