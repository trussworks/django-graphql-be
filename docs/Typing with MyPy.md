# Typing with MyPy

Our strategy for typing with mypy is to start strict and be intentional about any loosening of rules. We want all first party code to be type-hinted and only third-party modules to be exempted.

Slides detailing this info and more : [Typing with MyPy](https://docs.google.com/presentation/d/1XnNsNR4RAP9ddhJq4TNTgls2q8aBS4pe3hrk86noZq4/edit#slide=id.g103e285e760_0_391)

## Rules

1.  All first-party code (aka code we write) **must** **be** type-hinted.
2.  Only third-party modules **may be** exempted, and only if we cannot find suitable type hints.
3.  No explicit `Any`s **should be** introduced in first-party code.

## Strategies

### How to exempt a third-party module

1.  Try to find and install the stubs

    - Sometimes called `*-stubs` (`graphene-stubs`)
    - Sometimes called `types-*` (`types-pytz, types-pyyaml`)
    - For Python libraries, try `mypy --install-types`
    - For third party libraries, look in [typeshed](https://github.com/python/typeshed).

2.  If you cannot find type annotations:

    - Exempt the module using `ignore-missing-imports` in `.mypy.ini`

    ```bash
        [mypy-graphene_django.*]
        ignore_missing_imports = True
    ```

    - Add a ticket to annotate/stub the module in the future and a comment pointing to the ticket.

      ```bash
      [mypy-snapshottest.*]
      # SnapshotTest has no stubs
      # Ticket to revisit SP-100
      ignore_missing_imports = True
      ```

3.  When you need to use this module in the code, add a comment to disable the `[no-any-imported]` error. This will warn readers that there is an implicit `Any` on that line.

    `class HelloTestCase(SnapshotTestCase): # type: ignore[no-any-unimported]`

### How to write stubs for a third-party module

Once you start adding stubs for a module, **you must stub** _**everything**_ **that has been imported from said module.** If you don’t, you will start seeing `error: Module "<module>" has no attribute "<thing you didn't stub>" [attr-defined]` errors from `mypy`.

If you must add linter exceptions in the process, you must also track these exceptions in Jira so they can be revisited later.

1.  Once you’re ready to work on stubbing a third-party module, add a file or a directory to the `stubs/` directory.

    - If only adding a file, its name should be `<module>.pyi`, e.g. `stringcase.pyi`
    - If adding a directory, its structure should be `stubs/<module>/__init__.pyi` plus any additional `.pyi` files needed. Ex:

      ```
      stubs/
          |-- snapshottest/
          | |-- __init__.pyi
          | |-- pytest.pyi
      ```

2.  Write your stubs as if you were annotating your own functions/classes. Use `...` instead of writing the body of your functions.

    ```python
    """Types for code imported from the stringcase module"""

    def snakecase(string: str) -> str: ...
    ```

3.  For classes, **you do not need to stub out every attribute.** Only stub the parts of the class we use in our codebase. This allows us to do the work gradually without putting in effort for functionality we’ll never use.

    - A first pass of a stubbed class might be:

      ```python
      from pytest import FixtureRequest

      class PyTestSnapshotTest:
          def __init__(self, request: FixtureRequest) -> None: ...
      ```

    - Later on, we can add attributes:

      ```python
      class PyTestSnapshotTest:
          snapshot_should_update: bool

          def __init__(self, request: FixtureRequest) -> None: ...
      ```

4.  As you fill in the stubs for a module, remove the `# type: ignore[no-any-unimported]` comments for code that has been stubbed.
5.  Once all use cases of a module have been stubbed, remove the `ignore_missing_imports = True` setting for this module in the `.mypy.ini` file.

## Resources

- [MyPy Documentation](https://mypy.readthedocs.io/en/stable/index.html)
  - [Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
  - [Kinds of Types](https://mypy.readthedocs.io/en/stable/kinds_of_types.html)
  - [MyPy Configuration File](https://mypy.readthedocs.io/en/stable/config_file.html)
- [Python Type Checking (Guide) – Real Python](https://realpython.com/python-type-checking/) (Very readable overview - a little dated)
- [Stanford Seminar - Optional Static Typing for Python](https://www.youtube.com/watch?v=GiZKuyLKvAA) (Guido Rossum presenting)
- [Greg Price - Clearer Code at Scale: Static Types at Zulip and Dropbox - PyCon 2018](https://www.youtube.com/watch?v=0c46YHS3RY8)
