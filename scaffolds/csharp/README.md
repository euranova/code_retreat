# C# Scaffold for Code Retreat

Workflow when using this scaffold:
1. Start the Docker container with the tools needed to build, run and test your solution (see below).
2. Edit your code using you favorite editor.
3. Run the unit tests inside the container using ``dotnet test``.

## Start the .NET CLI and .NET Core

Under Linux, run a bash shell inside the docker container from the terminal:

```Bash
./docker.sh
```

Or, under Windows, run a bash shell inside the docker container from PowerShell:

```
./docker.ps1
```

This will start an interactive Docker container with the .NET Core SDK. A volume to the current folder is mounted into 
this container (in '/app').

## Run the tests

```Bash
dotnet test
```

The results of the tests are reported in the standard output only.

## Hierarchy of directories

* `CodeRetreat.Model`: source code project
* `CodeRetreat.Tests`: test project
