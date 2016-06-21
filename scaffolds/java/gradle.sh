#!/bin/bash

SRC_DIR=$(cd "$(dirname "$0")/.."; pwd)
echo "${SRC_DIR}"
docker run --rm -u $(id -u):$(id -g) -v $(pwd):/usr/bin/app:rw java-gradle $@
