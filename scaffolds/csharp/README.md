# C# Scaffold for Code Retreat

## Install the .NET CLI and .NET Core

There are several options. The easiest way is to work with a docker image ready
with all the tools you need:

```Bash
docker build -t csharp-code-retreat .
```

The only downside is that you need to run the .NET CLI through Docker.

```Bash
docker run -it csharp-code-retreat
```

## Run the tests

```Bash
dotnet test
```

The results of the tests are reported in the standard output only.

## Hierarchy of directories

* `src/CodeRetreat`: source code project
* `test/CodeRetreat.Tests`: test project