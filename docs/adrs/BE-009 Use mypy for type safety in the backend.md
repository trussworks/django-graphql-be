# BE-009 Use mypy for type safety in the backend

**Status:** Accepted

**Drivers:** Sandy Wright

**Deciders:** Patrick Dickey, Lindsay Techel, Shimona Carvalho

**Decision Date:** 11/29/2021

## Context

[We’ve selected Django as our backend framework](https://truss-dds.atlassian.net/wiki/spaces/SPP/pages/18940054), which is built on Python. Python is a _dynamically typed_ programming language, or, more specifically, a _duck typed_ language. “Duck typing” refers to the phrase:

> If it looks like duck, walks like a duck, and quacks like a duck--it’s a duck.

Python infers data types based on how variables are used and raises type errors accordingly. For example, trying to divide a string type will cause an error. These errors will only occur at runtime, however.

_Static typing_ means that types are declared when a variable is created. These variables can only be this type from that point on. Languages that are statically typed are often compiled languages, and type errors are found at compile time instead of runtime.

The earlier a type error is revealed, the easier it is to resolve. This is one of the main advantages of static typing--errors are generally much easier to debug. Static types are also more secure and help prevent common incidents, such as buffer overflows. For SITH, a project that is very concerned about security, this is a big positive.

Although Python is not statically typed and is not considered a “type-safe” language, there are many tools that help enforce strict typing in the codebase.

[**Type hints**](https://docs.python.org/3/library/typing.html), a base Python feature, let us annotate function parameters, class attributes, and other variables with types.

Libraries like [**Mypy**](https://mypy.readthedocs.io/en/stable/index.html) take that a step further by allowing us to enforce type annotations and check for type errors before runtime. [Google](https://google.github.io/pytype/), [Microsoft](https://github.com/Microsoft/pyright), and [Facebook](https://pyre-check.org/) have each published competing libraries to meet this need, but `mypy` is by far the most mature and active framework of the bunch (11.9k stars on GitHub, vs. 3.5k, 7.4k, and 5.7k respectively).

Each of these options will significantly change how we interact with our backend codebase.

## Decision

### Use `mypy` for type checking in the backend

Static typing is the clear choice forward to SITH, since it will help make our codebase more secure and maintainable. We will want as much automatic enforcement of this as possible, and `mypy` is our best option for doing so.

## Consequences

We will need to configure the backend with `mypy` and update any existing code to be compliant with its rules. **We will be following the guidelines outlined in** [Professional-grade mypy configuration - Wolt Blog](https://blog.wolt.com/engineering/2021/09/30/professional-grade-mypy-configuration/) **for our configuration.**

## Options Considered

### Use `mypy` for type checking

- `+` Configurable, and can enforce type annotations in the code
- `+` Checks for logical type errors at build/compile time instead of runtime
- `+` Has plugins for many IDEs that enable auto-checking and linting, making development easier
- `+` Follows the growing standard in web development to prioritize type safety
- `+` More secure and reliable than other options
- `-` Adds another dependency to the project
- `-` Still has some quirks and can be tricky to set up properly
- `-` Does not play well with Py2-compatible libraries, so it might affect what kinds of tools we can use in the future

### Enforce type hinting through code review

- `+` Type hinting is a base Python feature, so we don’t need to install any new libraries and further complicate dependencies
- `-` Humans miss things in code reviews, it is one of our species' many faults
- `-` Not enforced by default, would need to configure a linter to get any kind of assurance
- `-` Logical type errors will still only be discovered at runtime

### No type checking

- `+` Freedom!!
- `-` More buggy, and more difficult to debug
- `-` Less secure
- `-` Code is less informative and readable

## Resources

- [https://www.cs.cornell.edu/courses/JavaAndDS/files/strongWeakType.pdf](https://www.cs.cornell.edu/courses/JavaAndDS/files/strongWeakType.pdf)
- [GitHub - python/mypy: Optional static typing for Python](https://github.com/python/mypy)
  - [GitHub - google/pytype: A static type analyzer for Python code](https://github.com/google/pytype)
  - [GitHub - microsoft/pyright: Static type checker for Python](https://github.com/Microsoft/pyright)
  - [GitHub - facebook/pyre-check: Performant type-checking for python.](https://github.com/facebook/pyre-check)
- [typing — Support for type hints — Python 3.10.2 documentation](https://docs.python.org/3/library/typing.html)
- [PEP 483 -- The Theory of Type Hints](https://www.python.org/dev/peps/pep-0483/)
- [Python Type Checking (Guide) – Real Python](https://realpython.com/python-type-checking/)
- [Professional-grade mypy configuration - Wolt Blog](https://blog.wolt.com/engineering/2021/09/30/professional-grade-mypy-configuration/)
