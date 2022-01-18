# BE-010 Backend Code Formatter is Yapf

**Status:** Accepted

**Drivers:** Shimona Carvalho

**Deciders:** Sandy Wright, Lindsay Techel, Patrick Dickey

**Decision Date:** 12/1/2021

## Context

We’d like to have a code formatter that handles both pep8 compliance and making all the code formatting consistent.

## Decision

Let’s use **Yapf**. Black is too opinionated and often makes code less readable but doesn’t allow for any configuration. Autopep8 doesn’t really worry about style. So Yapf in autopep8 mode is probably a good balanced solution. It tries to be pep8 compliant, also does style reformatting and should we dislike certain choices, we can massage it slightly to ensure it’s readable. This gives us the best of both worlds.

## Consequences

All code will be autoformatted - we’ll start with a vanilla autopep8 setup.

## Options Considered

### Black

An opinionated code formatter

- `+` No settings (other than line length) - so turn it on and there are no more decisions to make.
- `-` No settings - so if it makes code harder to read or not pep8 compliant, no way to adjust.
- `-` Won’t make semantic changes to be pep8 compliant.

### Yapf

A code formatter with several modes and knobs

- `+` Has some base modes + knobs so if we want to change some settings we can.
- `+` Tries very hard to be pep8 compliant without changing semantics of code.
- `-` Won’t make semantic code changes to be pep8 compliant.

### Autopep8

A formatter that focuses on pep8 compliance, over readability and formatting.

- `+` Will make aggressive semantic changes to be pep8 compliant.
- `-` Does not focus on style formatting.

## Resources

- [The 3 best auto formatters for Python](https://www.kevinpeters.net/auto-formatters-for-python)
- [GitHub - google/yapf: A formatter for Python files](https://github.com/google/yapf)
- [autopep8](https://pypi.org/project/autopep8/)
- [The uncompromising code formatter — Black 21.12b0 documentation](https://black.readthedocs.io/en/stable/)
