# Invoke

PyInvoke is a python package that we will use for various tools and scripts.

Here are some tips on using it.

## List Tasks

```bash
> inv -l
Available tasks:

  build.mypy      Runs the mypy typecheck on all python folders
  db.check        Check that you can connect to the database in the docker container
  db.create       Create the database in the docker container
  db.destroy      Destroy the database and the docker container
  db.start (db)   Restart (or create) the docker container with the database
```

### Detailed help

For more help on a task, use its name followed by `-help`

`inv db.start -help`

### Default task

In the task list, the `(db)` after the command `db.start` tells you that task is aliased by `db`, so you can run it by just typing:

`inv db`

This is called a “default task” in the Invoke documentation and is a useful way to indicate and recommend the most useful tasks.

Read more on [invoke tasks here](https://docs.pyinvoke.org/en/stable/api/tasks.html).

## Autocompletion

Getting your shell to autocomplete your invoke commands makes running them even easier.

Invoke provides an easy way to generate the autocompletion script.

Run the following and save to a file. Your shell options are `(bash|zsh|fish)`.

`inv --print-completion-script=bash > inv_completion.bash`

Then source that file in your in your `.bashrc`

`. ~/inv_completion.bash`

Open a new terminal and you should be able to tab-complete any invoke commands.

`inv db 2db db.check db.create db.destroy db.start`
