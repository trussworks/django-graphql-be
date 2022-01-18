# BE-008 Task runner is PyInvoke

**Status:** Accepted

**Drivers:** Shimona Carvalho

**Deciders:** Sandy Wright, Lindsay Techel, Patrick Dickey

**Decision Date:** 11/22/2021

## Context

It’s useful to have a single tool that lets us run the various commands involved in setting up the database, cleaning builds, etc. Oftentimes a makefile is used, leveraging the `PHONY` syntax to achieve this.

## Decision

### Use PyInvoke.

Both invoke and pypyr seem very promising and in comparison, enable similarly succinct and readable code. The slight tilt in Invoke’s favor is that it’s been around longer, has more current users and contributors and is in a more stable state of development. Pypyr is actively in development and had api breaking changes as recently as 2 days ago from the writing of this ADR.

## Consequences

We should be able to build up a tool that simplifies discovery and running of simple tasks like managing the dev database state.

## Options Considered

### Makefile

Makefile is a way to specify tasks and prerequisites

- `+` Well-documented, has been in use for a very long time.
- `+` Builds a dependency graph and can be clever about which commands to execute
- `-` Has its own fairly hard-to-read syntax
- `-` Difficult to break into smaller files, tendency to turn into a giant file with lots of global variables
- `-` Is not self documenting, not easy to learn new commands

### Invoke

Invoke is a python package to build a command-line tool with tasks and prerequisites

- `+` [Well-documented](https://www.gnu.org/software/make/manual/make.html)
- `-` Relatively new compared to make (2014)
- `+` Reasonably large userbase (9k according to github)
- `+` Language is Python which we are already using for the backend
- `*` Requires python (which means it requires python and python pkg management) but we already have this requirement
- `+` Good documenting/discovery features such as help/usage information
- `+` Allows tasks to list pre and post-requisites

### Pypyr

Pypyr is a python package that uses a yaml file to define a pipeline of tasks

- `+` Well-documented
- `-` Relatively new compared to make (2017)
- `+` Still quite a small userbase (30 according to github)
- `*` Requires learning a new syntax but it is yaml so a well-understood format
- `*` Requires python (which means it requires python and python pkg management) but we already have this requirement
- `+` Pipeline concept can be easy to understand for most users, as it is also used in other tools
- `+` Allows pipeline to build flows on smaller steps

## Resources

- [GNU make](https://www.gnu.org/software/make/manual/make.html)
- [Welcome to Invoke! — Invoke documentation](https://www.pyinvoke.org/)
- [Quick start help guide to the pypyr pipeline task-runner.](https://pypyr.io/docs/getting-started/)
