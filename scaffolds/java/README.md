# Java Scaffold for Code Retreat

## Option 1: use docker wrapper scripts

See `scripts/` folder.

## Install Java and Gradle

There are several options. The easiest way is to work with a docker image ready
with all the tools you need.

The only downside is that you need to run gradle through Docker. To make it easy, \
we wrote a script `gradle` wrapping the `docker` command and acting as gradle.

## Run the tests

```Bash
./gradle test
```

## Run the app

```Bash
./gradle run
```

The results of the tests are reported both in the standard output and the following file `build/reports/tests/index.html`.

## Clean

```Bash
./gradle clean
```

## Hierarchy of directories

* `src/main/java`: source code
* `src/test/java`: the tests
* `build`: the generated binaries, jars, etc
