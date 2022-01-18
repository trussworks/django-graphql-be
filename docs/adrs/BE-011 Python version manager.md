# BE-011 Python version manager

**Status:** Accepted

**Drivers:** Sandy Wright

**Deciders:** Patrick Dickey, Lindsay Techel, Shimona Carvalho

**Decision Date:** 12/6/2021

## Context

As engineers working on the same project, we need to ensure that our development environments are as similar as possible. Developing with different tool versions is one of the many issues that can lead to unexpected bugs, and it’s not uncommon for libraries and packages to only be compatible with specific versions of a tool.

Python, in particular, is a quagmire of versioning (illustrated by [a classic XKCD comic](https://xkcd.com/1987/)). The fact that MacOS comes with Python pre-installed but still defaults to the no-longer-supported version 2.7 certainly doesn’t help. Version managers are practically essential to wrangle this language into a consistently usable state.

We really only have two options for Python version managers:

- [**pyenv**](https://github.com/pyenv/pyenv), the ever reliable, almost official, Python-specific version manager, and
- [**asdf**](https://asdf-vm.com/), the glittering newcomer that aims to handle version management for _all_ tools.

## Decision

### Use `asdf` to manage Python versions

Honestly, it’s hard to go wrong with either option. `pyenv` is a well-established and respected tool in the Python community, and [asdf-python](https://github.com/danhper/asdf-python) (the required plugin for managing Python with `asdf`) leverages `pyenv` themselves to handle version management. In effect, you’re going with `pyenv` either way.

However, `asdf` gives us the opportunity to have consistency across tech stacks, and across projects. It also has a plugin to integrate with `direnv` ([asdf-direnv](https://github.com/asdf-community/asdf-direnv)), which is a utility that we often use regardless of the framework we’ve picked. `asdf` is a promising tool that has the potential to save us a lot of time and effort for future projects.

## Consequences

We will need to add a `.tool-versions` file to our backend repo, and write set up instructions for `asdf` in our README.

## Options Considered

### Use `pyenv`

- `+` The default option in the Python community - Google “python version management” and the first page will be all `pyenv`
- `+` Lots of support from a large, established user base
- `+` Easily integrates with `direnv`
- `+` Does version management well
- `-` Does not manage virtual environments particularly well (although this is not the tool’s main use case)
- `-` Only manages Python versions

### Use `asdf`

- `+` User base is growing rapidly and it’s gaining in popularity over other version managers
- `+` Handles version management for many tools and languages, not just Python
- `+` Has a dedicated plugin for `direnv`, `asdf-direnv`
- `+` Leverages `pyenv` under the hood
- `-` No virtual environment or dependency management (although, again, this is not the intended purpose for this tool)
- `-` Marginally less support than `pyenv`
- `-` `asdf-python` is managed by a third-party dev, not `asdf-vm`

### No version management

- `+` Everyone gets to do what they want, Wild West style
- `-` Python versioning on MacOS remains a spiderweb of doom
- `-` Collaborative development becomes an endless cycle of “Well… It works on my machine.” and everyone slowly dies inside

## Resources

- [GitHub - pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv)
  - [Managing Multiple Python Versions With pyenv – Real Python](https://realpython.com/intro-to-pyenv/)
  - [Managing Python Environments with direnv and pyenv](https://stackabuse.com/managing-python-environments-with-direnv-and-pyenv/)
- [GitHub - asdf-vm/asdf: Extendable version manager with support for Ruby, Node.js, Elixir, Erlang & more](https://github.com/asdf-vm/asdf)
  - [GitHub - danhper/asdf-python](https://github.com/danhper/asdf-python)
  - [GitHub - asdf-community/asdf-direnv: direnv plugin for the asdf version manager](https://github.com/asdf-community/asdf-direnv)
  - [asdf: a version manager to rule them all](https://www.codegram.com/blog/asdf-version-manager-to-rule-them-all/)
  - [Switching to ASDF version manager](https://sidneyliebrand.io/blog/switching-to-asdf-version-manager)
  - [Switching from pyenv, rbenv, goenv and nvm to asdf - @yujinyuz](https://jinyuz.dev/posts/tips-and-tricks/Switching-from-pyenv,-rbenv,-goenv-and-nvm-to-asdf)
