# BE-004 Backend Unit Testing using PyTest

**Status:** Accepted

**Drivers:** Sandy Wright

**Deciders:** Patrick Dickey, Lindsay Techel, Shimona Carvalho

**Decision Date:** 11/18/2021

## Context

We have decided to try out Django as our backend framework, and now we need to decide on a framework for building our backend unit tests. Django offers many built-in testing tools that are convenient extensions of the standard Python testing library, `unittest`, but there are other frameworks that could help improve the testing experience. The frameworks I looked at are outlined in [Options considered](#options-considered).

## Decision

### Use PyTest as our backend testing framework.

PyTest does a fantastic job with _actually improving the testing experience_. It’s a tool that actually focuses on making the process simpler instead of prioritizing complicated new features. It should help make backend testing more accessible to everyone on the team.

## Consequences

We will need to install `pytest-django` as a dependency to our backend. We should also take this decision into consideration when selecting integration testing tools.

## Options Considered

[PyTest](https://docs.pytest.org/en/stable/)

- `+` Designed to _simplify_ testing, instead of adding a bunch of complicated new features.
- `+` Integrates with many other testing tools, such as [django-webtest](https://docs.pylonsproject.org/projects/webtest/en/latest/) (and [graphene-django](https://docs.graphene-python.org/projects/django/en/latest/testing/)!).
- `+` Lots of community support.
- `+` Experience with it on the team.
- `*` Has a [specific version](https://pytest-django.readthedocs.io/en/latest/tutorial.html) to integrate with Django (nice, but confusing).
- `-` Not the flashiest tool, most of its benefits are subtle.

### [Testify](https://github.com/Yelp/Testify)

- `+` Extends `unittest` (the standard Python testing library) and `nose` (another popular testing extension).
- `-` _**The team developing it literally switched to using PyTest themselves.**_

### [Robot](https://robotframework.org/)

- `+` Robust testing framework that supports acceptance and _system_ testing.
- `-` So many features related to robotic process automation, which we don’t need. The functionality we would use from this huge framework barely scratches the surface.

### No extra framework; use the testing tools Django gives us.

- `+` No extra dependencies or configuration.
- `-` Not as easy or seamless to run tests. Would have to write more boilerplate.

## Resources

- [pytest: helps you write better programs — pytest documentation](https://docs.pytest.org/en/stable/)
- [Getting started with pytest and pytest-django — pytest-django documentation](https://pytest-django.readthedocs.io/en/latest/tutorial.html)
- [Graphene-Python](https://docs.graphene-python.org/projects/django/en/latest/testing/)
