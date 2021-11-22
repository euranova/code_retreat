# Ruby Scaffold for Code Retreat

## Option 1: use docker wrapper scripts

This scaffold comes with severals tools that work with docker under the hood.
- `ruby`: a ruby 3 executable
- `bundler`: a ruby dependencies manager
- `minitest`: a ruby test framework

Run
```bash
./docker.sh [irb|ruby|rake]
```

See `scripts/` folder.

## Install the dependencies

```Bash
bundle install
```

## Run the tests

```Bash
rake
```

## Hierarchy of directories

* `spec`: the root of tests, you put your helper there
* `spec/dummy`: the tests are organized by directories, usually the name of
  the lib, or when you do the distinction between unit and integration tests
* `lib`: the source of your lib
