# Java Scaffold for Code Retreat

## Option 1: use Docker wrapper scripts

This scaffold comes with a pre-configured Docker environment.

### Run the tests
May need to pull the image (600MB) the 1st time.
```
./gradle.sh test
```
Or, using [TCR/BTCR](https://github.com/euranova/code_retreat#tcr):
```
./../../scripts/[tcr|btcr]
```

### Run the app

```
./gradle.sh run
```

## Option 2: use a locally installed Java environment
This option allows faster Gradle runs thanks to the Gradle daemon.
Java is required, for ex. 
[OpenJDK 11 tar.gz](https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz).

With this options, TCR/BTCR scripts will not be directly available because they use `./gradle.sh`
(which calls Docker). If you wish to use TCR without Docker, see the comments in `./scripts/`
sources so that it calls Gradle directly without wrapping in a Docker container.

### Run the tests

```
./gradlew test
```

### Run the app

```
./gradlew run
```

The results of the tests are reported both in the standard output and the following file `build/reports/tests/index.html`.

### Clean
Clears the `/build` folder.

```
./gradlew clean
```

## Hierarchy of directories

* `src/main/java`: source code
* `src/test/java`: the tests
* `build`: the generated binaries, jars, etc
