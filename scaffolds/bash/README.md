# Bash Scaffold for Code Retreat

## Option 1: use docker wrapper scripts

See `scripts/` folder.

## Install Test Framework Bats

```Bash
sudo aptitude install bats
```

## Run the tests

```Bash
bats test
```

## Run the app

```Bash
./bin/program
```

## Hierarchy of directories

* `bin`: the program
* `lib`: source code
* `test`: the tests
