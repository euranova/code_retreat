# note: add --priviledged if you wish to run the repl
docker run -it --rm -w /code -v $PWD:/code swiftdocker/swift $@
