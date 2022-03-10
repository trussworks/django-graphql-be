# Django GraphQL Backend

This project has an associated frontend that can be found here: [https://github.com/trussworks/next-graphql-fe](https://github.com/trussworks/next-graphql-fe)

## Usage

### Install tools with `asdf`

We use `asdf` to manage our tool versions. Currently, `asdf` manages:

- [Python](https://github.com/danhper/asdf-python)
- [direnv](https://github.com/asdf-community/asdf-direnv)
- [Poetry](https://github.com/asdf-community/asdf-poetry)

Install `asdf` using [the instructions in their official documentation](https://asdf-vm.com/guide/getting-started.html#getting-started).
This will involve a step to modify your shell profile file -- make sure you do this to complete the installation.
If you are unsure which of the instructions apply to you, reach out to the team and we'll help you figure it out.

You will also need to add the following plug-ins:

```shell
asdf plugin add python
asdf plugin add direnv
asdf plugin add poetry
```

Finally, `cd` into the repository folder and run:

```shell
asdf install
```

This will install the versions we have dictated in the `.tool-versions` file.

Your shell may prompt you to run additional commands to activate the newly installed tools. You may also need to restart your shell.

#### `direnv` additional steps

Direnv must also be added to your shell profile file (`.bashrc`, `.zshrc`, etc) to work properly. Follow [the official instructions](https://github.com/direnv/direnv/blob/master/docs/hook.md)
for whichever shell you use, and then change `direnv` to `asdf exec direnv`. If you use `zsh`, this will look like:

```shell
# Set in ~/.zshrc :
eval "$(asdf exec direnv hook zsh)"
```

Once you have finished updating your shell's profile file, run `direnv allow` to activate `direnv` in this folder.

### Install Python packages

This project is compatible with Python 3.9. We currently use `asdf` to manage our tool versions, and [Poetry](https://python-poetry.org/)
to manage our Python virtual environment.

First, make sure you install all the Python packages/dependencies with:

```shell
poetry install
```

The virtual environment for Poetry is created automatically when you install the dependencies. It is not, however,
activated automatically when you enter the repo.

There are two ways to interact with the virtual environment:

1. Use `poetry run <command>` to run commands within the virtual environment. For example, `poetry run inv -l` will list all of our invoke commands.
2. Use `poetry shell` to start a shell within the virtual environment. This is closest to the usual virtual environment experience. Use `poetry exit` or `deactivate` when you are done.

If you would like to configure your IDE interpreter to point at this virtual environment, use `poetry env info --path`
to get its path.

For more information about using Poetry, refer to their [official documentation](https://python-poetry.org/).

#### Using PyInvoke

This project uses [PyInvoke](https://www.pyinvoke.org/) to aggregate all useful commands and scripts. Run `invoke` or `inv` from the top level folder.

```sh
> inv -l
```

Read more about [invoke here](https://truss-dds.atlassian.net/wiki/spaces/eng/pages/50790405/Invoke).

### Install and Create Database

The database is a postgres container which runs inside a docker container.

First time running this project? Please run Docker and install postgres.

```sh
brew install postgres
```

Create and run the database using invoke

```sh
inv db.start
```

#### Migrate the Database

Once you've created a database, you'll need to apply our migrations so that you can use it:

```shell
python manage.py migrate
```

#### Load Test Data

After the database has been migrated, you can load our default fixture with test data:

```shell
python manage.py loaddata api/fixtures/default.json
```

### Run the Backend

Run the server

```sh
python manage.py runserver
```

You should be able to access the graphql browser at `http://127.0.0.1:8000/graphql`

The graphql query:

```graphql
query {
  hello
}
```

should respond with:

```json
{
  "data": {
    "hello": "Hello World!"
  }
}
```

## Typechecking

To typecheck the project, from the toplevel call

```sh
inv build.mypy
```

You should see no errors.

```sh
Success: no issues found in 3 source files
Success: no issues found in 14 source files
```

## Troubleshooting

### Asdf: BUILD FAILED installing python

**Issue:** Asdf fails to install a new python version

You may see an error like this...

```sh
>  asdf install python 3.9.1
...
python-build 3.9.1 /Users/shimona/.asdf/installs/python/3.9.1
python-build: use openssl@1.1 from homebrew
python-build: use readline from homebrew
Downloading Python-3.9.1.tar.xz...
-> https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tar.xz
Installing Python-3.9.1...
python-build: use tcl-tk from homebrew
python-build: use readline from homebrew

BUILD FAILED (OS X 12.0.1 using python-build 2.2.2-14-g381002db)

Inspect or clean up the working tree at /var/folders/tl/9m081bjx6sgb8s0zst8qyz280000gn/T/python-build.20211221173254.4843
Results logged to /var/folders/tl/9m081bjx6sgb8s0zst8qyz280000gn/T/python-build.20211221173254.4843.log
```

**Fix:** The issue is often with an incompatible build tool installed in xcode.
Try

```sh
>  xcode-select --install
```

Or, if that doesn't work, install the latest version of xcode commandline tools (12.5.1) from here
<https://developer.apple.com/download/all/?q=command%20line%20tools> (edited)

### Poetry install can't find postgres

**Issue:** If you used asdf for postgres, sometimes poetry is unable to find the right version.

```text
asdf: No version set for command pg_config
```

**Fix:** Setting the global version of asdf works although it's not an ideal fix.

```text
> asdf global postgres 12.7
```

### System is using wrong version of asdf

**Issue:** Typing command: `poetry shell` throws an asdf error. The error shows asdf trying to use `0.8.1_1`. Typing `asdf version` returns v0.9.0, which is a version mis-match.

```text
~/.asdf/shims/python: line 3: /usr/local/Cellar/asdf/0.8.1_1/libexec/bin/asdf: No such file or directory
```

**Fix:** Manually update [asdf shims](https://github.com/asdf-vm/asdf/issues/1115#issuecomment-1018009184)

```text
> rm ~/.asdf/shims/*
> asdf reshim
```

### Poetry dependencies are out of sync

Sometimes your dependencies just get all borked up. One of the easiest ways to set things right again is to burn it all down and do a fresh install.

To do so, you'll first need to remove the virtual environment that Poetry automatically created for the project. Find it with `poetry env list`.

Next, you should remove it with `poetry env remove <name-of-your-env-here>`.

Finally, run `poetry install` to make a new environment and re-install all the dependencies from scratch.
