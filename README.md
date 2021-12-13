# SITH Backend

The SITH backend is a django-based backend for the System for Insider Threat Hindrance (SITH) project

## Usage

### Install tools with `asdf`

We use `asdf` to manage our tool versions. Currently, `asdf` manages:

* [Python](https://github.com/danhper/asdf-python)
* [direnv](https://github.com/asdf-community/asdf-direnv)
* [Poetry](https://github.com/asdf-community/asdf-poetry)

Install `asdf` using [the instructions in their official documentation](https://asdf-vm.com/guide/getting-started.html#getting-started). 
This will involve a step to modify your shell profile file--make sure you do this to complete the installation. 
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

1. Use `poetry run <command>` to run commands within the virtual environment. For example, `poetry run inv -l` will list 
all of our invoke commands.
2. Use `poetry shell` to start a shell within the virtual environment. This is closest to the usual virtual environment 
experience. Use `poetry exit` or `deactivate` when you are done.

If you would like to configure your IDE interpreter to point at this virutal environment, use `poetry env info --path` 
to get its path.

For more information about using Poetry, refer to their [official documentation](https://python-poetry.org/).

#### Using PyInvoke

This project uses [PyInvoke](https://www.pyinvoke.org/) to aggregate all useful commands and scripts. Run `invoke` or `inv` from the top level folder.

```sh
> inv -l
````

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

### Run the Backend

Run the server

```sh
python server/manage.py runserver
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
