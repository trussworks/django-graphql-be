# SITH Backend

The SITH backend is a django-based backend for the System for Insider Threat Hindrance (SITH) project

## Usage

### Install tools with `asdf`

We use `asdf` to manage our tool versions. Currently, `asdf` manages:

* [Python](https://github.com/danhper/asdf-python)
* [direnv](https://github.com/asdf-community/asdf-direnv)

Install `asdf` using [the instructions in their official documentation](https://asdf-vm.com/guide/getting-started.html#getting-started). 
This will involve a step to modify your shell profile file--make sure you do this to complete the installation. 
If you are unsure which of the instructions apply to you, reach out to the team and we'll help you figure it out.

You will also need to add the following plug-ins:

```shell
asdf plugin add python
asdf plugin add direnv
```

Finally, `cd` into the repository folder and run:

```shell
asdf install
```

This will install the versions we have dictated in the `.tool-versions` file.

#### `direnv` additional steps

Direnv must also be added to your shell profile file to work properly. Follow [the official instructions](https://github.com/direnv/direnv/blob/master/docs/hook.md) 
for whichever shell you use, and then change `direnv` to `asdf exec direnv`. If you use `zsh`, this will look like:

```shell
eval "$(asdf exec direnv hook zsh)"
```

### Install Python Packages

This project is compatible with Python 3.9.

Create a virtualenv if you prefer (TBD Recommendation from project team)

Use the package manager `pip` to install the packages.

```sh
pip install -r requirements.txt
```

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
cd sith_django
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
