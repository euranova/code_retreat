# Javascript Scaffold for Code Retreat

## Install Java and Gradle

There are several options. The easiest way is to work with a docker image ready
with all the tools you need:

```Bash
docker build -t java-gradle .
```

The only downside is that you need to run gradle through Docker. To make it easy, we wrote a script `gradle.sh` wrapping the `docker` command and acting as gradle.

## Run the tests

```Bash
./gradle.sh check
```

## Run the app

```Bash
./gradle.sh run
```

The results of the tests are reported both in the standard output and the following file `build/reports/tests/index.html`.

## Clean

```Bash
./gradle.sh clean
```

## Hierarchy of directories

* `src/main/java`: source code
* `src/test/java`: the tests
* `build`: the generated binaries, jars, etc
