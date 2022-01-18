# BE-012 Python dependency and environment manager

**Status:** Accepted

**Drivers:** Sandy Wright

**Deciders:** Patrick Dickey, Lindsay Techel, Shimona Carvalho

**Decision Date:** 12/8/2021

## Context

Dependency management has been streamlined in many languages and frameworks with tools like `npm` or `yarn`, but it’s still a whole bag of worms when it comes to Python. Python uses `pip` to install third-party packages, but unlike `npm` or even Maven, `pip` defaults to installing tools globally. In order to keep your Python environment unsullied by the multitudes of packages you need for all your various projects, you have to use virtual environments to install them on a per-project basis. Python comes with the tools `venv` and `virtualenv` to do this.

So Python gives you all the tools you need for basic dependency management… technically. But it gets more complicated as you have to consider freezing the versions of dependencies of dependencies and so on. Some folks end up using 3+ tools, such as `pip`, `virtualenv`, `pip-tools`, `tox` and so on, to get their ideal setup. Others are content to lose some control and choose a tool that supercedes the Python defaults, replacing the headache with one command.

Either way, it’s an important decision to make early on in the development process to avoid security risks and a possible “dependency hell.” There are _numerous_ options out there to handle dependency management for Python, and I chose to go with the bundled options that would replace `pip` with alternate commands. These options were considerably simpler and cleaner to implement than the combined tooling approaches.

They include:

- [**Pipenv**](https://pipenv.pypa.io/en/latest/) - a dependency and virtual environment manager that has an almost-recommendation from Python in the official docs: [Managing Application Dependencies — Python Packaging User Guide](https://packaging.python.org/tutorials/managing-dependencies/)
- [**Poetry**](https://python-poetry.org/) - a dependency manager that has a special focus on project management and also gets a shoutout in the official Python docs.
- [**Pyflow**](https://github.com/David-OConnor/pyflow) - a relatively new dependency manager that also handles Python versioning
- [**Conda**](https://docs.conda.io/en/latest/) - an alternate Python _ecosystem_ that uses the Conda package repository instead of PyPI.
- [**Hatch**](https://github.com/ofek/hatch) - another new-ish dependency manager that focuses on generated tests.

These articles are great comparative resources:

- [Python Tools for Managing Virtual Environments](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko)
- [Overview of python dependency management tools](https://modelpredict.com/python-dependency-management-tools)

## Decision

### Use Poetry for our backend dependency/environment manager

While there were numerous options, the main decision was between Pipenv and Poetry. While Pipenv is notably more established in the Python community than Poetry, Poetry seemed to out-class it in almost every other area.

Poetry is performant, it keeps up with Python community standards, and it plays well with `asdf`, [our chosen version manager](https://truss-dds.atlassian.net/wiki/spaces/SPP/pages/56950789). Almost every comparative article I read on these tools ended with a recommendation for Poetry. The most notable loss would be the lack of built-in support for Poetry in GitHub Actions, but there are [numerous actions in the marketplace](https://github.com/marketplace?type=actions&query=poetry+) that aim to fill this gap.

## Consequences

Our backend was set up with Pipenv as the recommendation for version manager. This ADR would change that, so we would need to update our config files and instructions for setting up our dev environments with Poetry instead. This should not be a dramatic change, but it will probably be tedious.

## Options Considered

### Pipenv

- `+` Creates a virtual environment automatically
- `+` Automatically updates the Pipfile with new dependencies
- `+` Can generate a `requirements.txt` with the dependencies installed
- `+` GitHub Python actions have built-in support for Pipenv
- `-` In the past few years, has had flaky development cycles
- `-` Installs _before_ locking dependencies, meaning Pipenv will only notify you of a dependency failure after it has been installed to your system
- `-` Does not use `pyproject.toml`, which [Python has decided is the config file of choice for Python projects](https://www.python.org/dev/peps/pep-0621/)

### Poetry

- `+` Can do everything Pipenv can do, and:
- `+` Uses the `pyproject.toml` file as the config file, which is Python’s official choice for config
- `+` Development cycles are consistent (roughly 1 minor release per month)
- `+` [More performant than Pipenv](https://dev.to/frostming/a-review-pipenv-vs-poetry-vs-pdm-39b4)
- `+` `asdf` has a [semi-official plugin for Poetry](https://github.com/asdf-community/asdf-poetry)
- `-` Fewer stars than Pipenv (~17k vs 22k)
- `-` Not built-in to GitHub Actions, would need to manually add it to workflows

### Pyflow

- `+` Handles Python versioning as well
- `-` _Very_ new, less than 1k stars on GitHub
- `-` We’re using [asdf for Python versioning](https://truss-dds.atlassian.net/wiki/spaces/SPP/pages/56950789)

### Conda

- `+` Gives access to the Conda package ecosystem
- `+` Great for data scientists
- `-` Lots of overhead, this is a dramatic change in our Python environment
- `-` [PyPI has ~150,000 packages, Conda has ~1500](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko#conda)

### Hatch

- `+` Proactive approach to testing
- `-` Doesn’t automatically update any config files like `tox.ini` or `requirements.txt`

### Use Python defaults `pip` and `venv` to manage dependencies

- `+` No need to install additional tools
- `-` Doesn’t freeze second-degree dependencies, vulnerable to security holes

## Resources

- [Python Tools for Managing Virtual Environments](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko)
- [Overview of python dependency management tools](https://modelpredict.com/python-dependency-management-tools)
- [Managing Application Dependencies — Python Packaging User Guide](https://packaging.python.org/tutorials/managing-dependencies/)
- [Why requirements.txt isn’t enough](https://modelpredict.com/wht-requirements-txt-is-not-enough)
- [Best Practices for Python Dependency Management](https://medium.com/knerd/best-practices-for-python-dependency-management-cc8d1913db82) → outlines a combined tooling approach (`pip` + `venv` + `pip-tools` + `tox`). Clearly it's very involved, and it seems to best suited for building Python packages, not web apps.
- Comparing Pipenv and Poetry:
  - [Comparison of Pip, Pipenv and Poetry dependency management tools](https://remastr.com/blog/pip-pipenv-poetry-comparison)
  - [A Review: Pipenv vs. Poetry vs. PDM](https://dev.to/frostming/a-review-pipenv-vs-poetry-vs-pdm-39b4)
  - [Pipenv and Poetry: Benchmarks & Ergonomics](https://johnfraney.ca/posts/2019/03/06/pipenv-poetry-benchmarks-ergonomics/)
