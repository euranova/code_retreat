# C# Scaffold for Code Retreat

## Option 1: use docker wrapper scripts

See `scripts/` folder.

## Otherwise: Workflow

Workflow when using this scaffold:

1. Start the Docker container with the tools needed to build, run and test your solution (see below).
2. Edit your code using you favorite code editor.
3. Run the unit tests inside the container using ``dotnet test .\CodeRetreat.Tests\``.
4. (optional) Run the application inside the container using ``dotnet run --project .\CodeRetreat.Console\``.

## Start the .NET CLI and .NET Core

Under Linux, run a bash shell inside the docker container from the terminal:

```Bash
./dotnet-env.sh
```

Or, under Windows, run a bash shell inside the docker container from PowerShell:

```
./dotnet-env.ps1
```

This will start an interactive Docker container with the .NET Core SDK. A volume to the current folder is mounted into
this container (in '/app').

## Run the tests

```Bash
dotnet test .\CodeRetreat.Tests\
```

The results of the tests are reported in the standard output only.

## Run the application

```Bash
dotnet run --project .\CodeRetreat.Console\
```

The results of the tests are reported in the standard output only.

## Hierarchy of directories

* `CodeRetreat.Console`: console project that runs the model
* `CodeRetreat.Model`: source code project
* `CodeRetreat.Tests`: test project
