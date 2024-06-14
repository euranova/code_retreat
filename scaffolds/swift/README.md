# Swift scaffold

This scaffold is not complete yet, but does introduce an env in which swift
code can be compiled and run.

## Examples

Run the code :
```
./swift-env.sh swift hello.swift
```

Compile & run :
```
./swift-env.sh swiftc hello.swift

./swift-env.sh ./hello
```

## REPL

The REPL requires a priviled container. Use this :
```
docker run -it --rm --privileged -w /code -v "${PWD}":/code swiftdocker/swift:3.0.1 swift
```
