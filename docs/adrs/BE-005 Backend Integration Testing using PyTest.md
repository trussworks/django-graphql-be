# BE-005 Backend Integration Testing using PyTest

**Status:** Accepted

**Drivers:** Shimona Carvalho

**Deciders:** Sandy Wright, Lindsay Techel, Patrick Dickey

**Decision Date:** 11/9/2021

## Context

Integration tests test that the whole system works together and are necessary to detect issues when one part of the system that is under development breaks another part of the system. It’s important to note that unit tests will provide the first level of coverage and integration tests are not expected to test every possible case.

## Decision

### Decision is to use **Pytest**.

Additionally, one consideration in the selection of integration testing mechanisms is how to handle database access. To create a test, one must often populate the database with baseline data. Preloading the database means that tests are not self-contained. In addition, this data can cause issues if it drifts away from the active business logic. To that end, we recommend using a factory package such as FactoryBoy or ModelMommy to create the objects on which the tests are run.

## Consequences

Not many. Pytest gives us all the flexibility we need. The only real catch is that we must make sure to track the dependency and updates.

## Options Considered

### Pytest

- `+` More succinct tests, simplifies testing
- `+` Plenty of community support
- `+` Team has experience with it
- `+` Built on top of unittest so we get all of unittest functionality
- `+` We have selected Pytest for backend unit tests. [Relevant ADR](./BE-004%20Backend%20Unit%20Testing%20using%20PyTest.md)
- `-` Not part of standard library, it’s a dependency

### Unittest

- `+` Part of the standard library, no dependencies
- `-` More boilerplate required, longer development time

### Robot

- `*` Good for heterogeneous environments, and cross platform applications (not our usecase)
- `-` Has its own syntax which will have its own learning curve
- `-` No team experience
- `*` Great for robotics applications (not our usecase)

## Resources

- [pytest: helps you write better programs — pytest documentation](https://docs.pytest.org/en/stable/)
- [Effective Python Testing With Pytest – Real Python](https://realpython.com/pytest-python-testing/)
