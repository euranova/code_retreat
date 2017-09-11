# C++ Scaffold for Code Retreat

This code scaffold uses [CxxTest](http://cxxtest.com). We recommend using the
docker image [euranova/cxxtest](https://github.com/euranova/docker-cxxtest), but
installing `cxxtest` with the package manager is also an option.

## Start docker image

Start a bash prompt in the docker image, with the code mounted as a volume:

```bash
docker run --user ${UID} -it -v ${PWD}:/app euranova/cxxtest
```

## Run the tests

In order to run the tests, execute the following command:

```bash
make test
```

`make` does the following:
- parse the test file (in our case [test/Tests.h](test/Tests.h)) using
`cxxtestgen` and generate the C++ code for the test runner,
- build the test runner along with the code to be tested using `g++`,
- run the test executable.

## Clean

To remove the _build_ folder, which contains all the generated files:

```bash
make clean
```

## Writing tests

When writing tests, it is important to keep the _src-files_ and _header-files_
constants updated in the Makefile if new files are added or removed.

For more information about CxxTest assertions, see
[CxxTest's documentation](http://cxxtest.com/guide.html#_a_first_example)


### Warning

When using `cxxtestgen` with the `--fog-parser` option, the following warning is
displayed:
```
WARNING: Couldn't create 'cxxtest.parsetab'.
[Errno 13] Permission denied: '/cxxtest/python/python3/cxxtest/parsetab.py'
```

This warning can safely be ignored.
