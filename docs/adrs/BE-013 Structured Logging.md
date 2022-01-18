# BE-013 Structured Logging

**Status:** Accepted

**Drivers:** Shimona Carvalho

**Deciders:** Sandy Wright, Lindsay Techel, Patrick Dickey

**Decision Date:** 1/7/2022

## Context

We are currently just printing logs but in the interest of deploying to AWS, we should switch this over to structured logging in JSON.

Structured Logging is not only structuring your logging using an object that can be parsed by down-the-line services like Cloudwatch, but also being standardized in your logging. For e.g. logs including a user id should all be using `user_id` as the key and not `userID`, `user-id`, `user`, etc.

This kind of structure and standardization can improve

- Searching and filtering logs
- Understanding logs and debugging when an incident happens
- Integrating the logs with tools such as CloudWatch, Kibana etc…

Basically it makes logs easier to consume by both humans and machines.

## Decision

### We’ll use **Python logging**.

It is flexible enough to cover our needs, and should we want to integrate with other services (like openTelemetry), it’s the most likely package to be supported out of the box.

## Consequences

We’ll have our logs switch out to json, which may make them harder to read but is invaluable for cloudwatch. We could also customize the local dev logs to be easier to read (highlight the “msg” vs the details). We should also document a standardized log template as we start to actually build out the system.

## Options Considered

### [Structlog](https://www.structlog.org/en/stable/why.html)

- `+` Structures the logs using json which is well known and standardized
- `+` More complex setup possible using the processors and binding
- `+` Ability to format in any way and pass to a variety of outputs
- `-` More complex might be overkill for what we need

### [Python logging module](https://docs.python.org/3/library/logging.html)

- `+` Structures the logs using json which is well known and standardized
- `+` Ability to format in any way and pass to a variety of handlers (file, stdout, etc.)
- `+` Very well known package that's part of the python standard library
- `+` Future integrations (possibly with openTelemetry) will likely easier since this is the default Python package
- `-` Does not do JSON out of the box but is relatively easy/common to configure using custom handlers

### [OpenTelemetry](https://opentelemetry.io/status/)

- `-` Currently this aspect of openTelemetry is under development.
- `+` Would be great to use the one tool for both normal logs and traces for telemetry.

## Resources

- [structlog: Structured Logging for Python](https://www.structlog.org/en/stable/why.html)
- [Why you should be using structured logs - Stefan Krawczyk](https://www.youtube.com/watch?v=4Y3VdS2pLF4&t=544s)
- [OpenTelemetry Status](https://opentelemetry.io/status/)
