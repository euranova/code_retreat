# Scala Scaffold for Code Retreat

## Install scala tools

* Java: make sure you have a JDK installed on your machine!
* SBT: [Follow the instructions](http://www.scala-sbt.org/download.html).

The alternative is to use a docker image (see "Run with docker").

## Run the tests

```bash
sbt test
```

## Run the app

```bash
sbt run
```

## Run with docker

If you have docker installed, you can do the following :

```bash
docker build -t euranova/scala-sbt .
```

Then you can run sbt

```bash
docker run -it --rm -v $PWD:/root/project -w /root/project euranova/scala-sbt sbt [COMMAND]
```

`COMMAND` could be 'run' or 'test'. You can also skip that argument, which will bring you to a console
where you can also type `run` or `test`.


## Hierarchy of directories

* `src`: source code
* `test`: the tests
