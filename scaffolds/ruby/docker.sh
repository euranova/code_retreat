#!/bin/bash

ENABLE_TTY=${ENABLE_TTY:--t}
IMAGE="code-retreat-ruby-env"
VERSION="1"
TAG="$IMAGE:$VERSION"

docker images | grep -q "$IMAGE[ ]*$VERSION" || docker build -t $TAG .
docker run --rm -i ${ENABLE_TTY} -v $PWD:/usr/src/app -w /usr/src/app -u $(id -u):$(id -g) $TAG $@
