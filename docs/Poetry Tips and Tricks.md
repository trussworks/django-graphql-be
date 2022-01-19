# Poetry Tips and Tricks

## How to load the poetry shell with direnv

You can load the poetry shell simply on entering the folder! Here’s how.

First you want to add this function to a file called `.direnvrc` in your home directory (`/home/<username>/` with these contents.

This adds a function called `layout poetry` that any direnv has access to.

```python
function layout_poetry() {
  if [[ ! -f pyproject.toml ]]; then
    log_error 'No pyproject.toml found. Use `poetry new` or `poetry init` to create one first.'
    exit 2
  fi

  # create venv if it doesn't exist
  poetry run true

  export VIRTUAL_ENV=$(poetry env info --path)
  export POETRY_ACTIVE=1
  PATH_add "$VIRTUAL_ENV/bin"
}
```

Then in your `<sith-backend>/.envrc.local` which should be loaded by the version controlled `.envrc` you can call the function

`layout poetry`

Then simply reload the config using `direnv allow`.

When you change directory in and out of the `<sith-backend>` folder, it should activate and deactivate the poetry shell.
