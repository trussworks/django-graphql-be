# Python Best Practices

Generally, we’ll be following PEP8. These guidelines are robust, well-considered, and there are many linters and formatters that enforce them.

This guide outlines some basic rules so folks can get started, but it does not reiterate all of PEP8. Exceptions to PEP8 are highlighted at the end.

## Contents

- [Principles](#principles)
- [Formatting](#formatting)
  - [Naming conventions](#naming-conventions)
  - [White space](#white-space)
  - [Organization](#organization)
- [Syntax](#syntax)
  - [General](#general)
  - [Comments](#comments)
  - [Type hints](#type-hints)
- [PEP8 Exceptions](#pep8-Exceptions)
- [Terms](#terms)
- [Resources](#resources)

## Principles

- The Golden Rule of development: Build tools for others that you want to be built for you.
- Write code for humans, not computers. Readability matters.N
- Write documentation as you go.N
- Check for tools and packages in PyPI before duplicating work.
- Fix broken code before adding new functionality.
- Don’t bury errors. When in doubt, raise the exception.
- Test as if you’re shooting for 100% code coverage, but don’t focus on the percentage.

## Formatting

### Naming conventions

Variables and functions

`snake_case`

Constants

`SCREAMING_SNAKE_CASE`

Classes

`PascalCase`

Protected methods and attributes

_i.e. functions or variables of a class or package that should not be used outside of that class or package_

`_prefixed_with_underscore`

- Avoid obscure, short variable names unless their reference is already clear, such as in a for loop or except clause.

  **No**

  `e = runtime.Environment()`

  **Yes**

  `environment = runtime.Environment()`

  **Yes**

  ```python
  try:
    create_environment()
  except TypeError as e:
    log(e)
  ```

- Avoid redundancy in naming.

  **No**

  `Book.book_author`

  **Yes**

  `Book.author`

### White space

- Indent with 4 spaces instead of tabs.
- Surround every class and file-level function definition with two blank lines.
- Surround every class method with one blank line.
- Put one blank line between disparate blocks of code. For example, between the imports and a top-level constant definition. Use your best judgment.

### Organization

- Imports should be grouped into three sections, in order from top to bottom:

  1. Imports from Python built-in packages.
  2. Imports from dependencies and third-party tools installed with `pip`
  3. Local imports from within your codebase.

  Each section should be separated by one blank line:

  ```python
  # -*- coding: utf-8 -*-
  import os
  from typing import Optional

  import faker

  from .models import DataModel
  ```

## Syntax

### General

- [**Codementor’s Pythonic Code Guide**](https://www.codementor.io/blog/pythonic-code-6yxqdoktzt) → highly recommended
- Avoid getter and setter methods.

  **No**

  `person.set_age(54)`

  **Yes - direct access is the pythonic way to go:**

  `person.age = 54`

  Use `@property` decorator if getters or setters are absolutely necessary:

```python
class Book:
    def __init__(self, title: str) -> None:
        self._title = title

    @property
    def title(self) -> str:
        return title_case(self._title)

    @title.setter
    def title(self, value: str) -> None:
        self._title = value
```

- Reduce nesting wherever possible to improve readability.

  **No**

  ```python
  def do_something(a: int) -> int:
    if a > 10:
        return 1
    else:
        return 0
  ```

  **Yes**

  ```python
  def do_something(a: int) -> int:
    if a > 10:
        return 1

    return 0
  ```

- Never use mutable data types as default values in class or function definitions.

  **No**

  ```python
  class Book:
    terms: dict = {}
  ```

  **Yes, mutable types are okay when set in an `__init__` method:**

  ```python
    class Book:
    terms: Optional[dict] = None

    def __init__(self) -> None:
         self.terms = {}
  ```

### Comments

- Use docstrings on files, classes, and functions to document code as you go. Follow [PEP’s guidelines on formatting](https://www.python.org/dev/peps/pep-0257/).
- Use triple quotes `"""` instead of triple apostrophes `'''` for docstrings.
- Never use `"""` or `'''` for multi-line comments outside of a docstring. These symbols are not ignored by the interpreter, unlike `#` comments, and will increase memory usage.

  **No**

  ```python
  """
  This is a bad multiline comment.
  Lots of things to say.
  """
  ```

  **Yes**

  ```python
    # This is a good multiline comment.
    # Lots of things to say.
  ```

  **Yes**

  ```python
    def do_something() -> None:
    """This is a docstring--we love this!"""
  ```

### Type hints

- Use explicit type annotations instead of type comments whenever possible. Type comments are designed for compatibility with Python 2, which is only a concern with third-party packages.

  **No** (unless you’re working with a third-party package like `invoke`)

  ```python
  def circumference(radius):
    # type: (float) -> float
  ```

  **Yes**

  `def circumference(radius: float) -> float:`

  Type annotations also allow us to use the `__annotations__` dictionary on objects:

  ```python
  >>> circumference.__annotations__
  {'radius': <class 'float'>, 'return': <class 'float'>}
  ```

## PEP8 Exceptions

- Recommended line length is 120.
- Unused imports are acceptable in `__init__.py` files.

## Terms

**method**

A _method_ is a function that has been defined as part of a class.

**attribute**

An _attribute_ is a variable that has been defined as part of a class. It belongs to an object.

**instance (of a class)**

An _instance_ of a class is created, or _instantiated_, whenever the `__init__` method on the class is called. This happens when a class is assigned to a variable with the following syntax:

`my_object = Object()`

Without the parentheses, it is not an instance. You have just assigned the class _type_ to the variable:

`my_object_type = Object`

It can later be instantiated the same way:

`my_object = my_object_type()`

**property**

A _property_ is a value on a class that has `__get__`, `__set__`, or `__delete__` methods. It can act as one attribute, or encapsulate several attributes. It is defined using the `@property` decorator.

## Resources

- [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [The Hitchhiker’s Guide to Python! — The Hitchhiker's Guide to Python](https://docs.python-guide.org/)
- [Python Best Practices: 5 Tips For Better Code](https://airbrake.io/blog/python/python-best-practices) - short, big picture overview
- [A "Best of the Best Practices" (BOBP) guide to developing in Python.](https://gist.github.com/sloria/7001839) - opinionated (and I don’t agree with everything) but still a good, easy-to-read outline
- [Python Best Practices – Real Python](https://realpython.com/tutorials/best-practices/) - comprehensive and helpful!
- [Python Type Checking (Guide) – Real Python](https://realpython.com/python-type-checking/)
