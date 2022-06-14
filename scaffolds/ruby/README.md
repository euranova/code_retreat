# Ruby Scaffold for Code Retreat

## Option 1: use Docker wrapper scripts

This scaffold comes with pre-configured Docker environment.

### Run the tests 
May take 1min. to build the image the 1st time.
```bash
./rake
```
Or, using [TCR/BTCR](https://github.com/euranova/code_retreat#tcr):
```
./../../scripts/[tcr|btcr]
```
## Option 2: use a locally installed ruby environment
With this options, TCR/BTCR scripts will not be directly available 
because they use `./gradle.sh` (which calls Docker). 
If you wish to use TCR without Docker, see the comments 
in `./scripts/` sources so that it calls Gradle directly without wrapping 
in a Docker container.

Ruby and Bundler 2+ are required.
### Install the dependencies

```Bash
bundle
```

### Run the tests

```Bash
rake
```

## Hierarchy of directories

* `spec`: the root of tests, you put your helper there
* `spec/dummy`: the tests are organized by directories, usually the name of
  the lib, or when you do the distinction between unit and integration tests
* `lib`: the source of your lib
