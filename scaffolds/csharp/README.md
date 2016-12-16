# C# Scaffold for Code Retreat

## Start the .NET CLI and .NET Core

Run a bash shell inside the docker container :

```Bash
./docker.sh
```
## Run the code

Once inside the docker container, you can do :

```Bash
cd src/CodeRetreat
dotnet restore
dotnet run
```

## Run the tests

```Bash
cd test/CodeRetreat.Tests
dotnet restore
dotnet test
```

The results of the tests are reported in the standard output only.

## Hierarchy of directories

* `src/CodeRetreat`: source code project
* `test/CodeRetreat.Tests`: test project
