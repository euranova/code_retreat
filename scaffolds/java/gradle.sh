#!/bin/bash

docker run --rm \
  -u $(id -u):$(id -g) \
  -v $(pwd):/home/gradle/project:rw \
  -w /home/gradle/project \
  gradle:7.4.2-jdk11-alpine gradle $@
