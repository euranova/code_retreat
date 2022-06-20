# Java Scaffold for Code Retreat

This scaffold uses a Gradle Wrapper if present, if not it uses Gradle, 
if Gradle is not installed it runs a Docker container.

It won't work with Gradle <5, to install a recent version, use
```
gradle wrapper
```

## Run the tests
```
./scripts/test
```
Or, using [TCR/BTCR](https://github.com/euranova/code_retreat#tcr):
```
./../../scripts/[tcr|btcr]
```

## Run the app

```
./gradle-env run
```

## Clean
Clears the `/build` folder.

```
./gradlew clean
```

## Hierarchy of directories

* `src/main/java`: source code
* `src/test/java`: the tests
* `build`: the generated binaries, jars, etc
