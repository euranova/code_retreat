#!/bin/bash

ENABLE_TTY=${ENABLE_TTY:--t}

docker run -i ${ENABLE_TTY} --rm -v ${PWD}:/app -w /app microsoft/dotnet:2.0.0-sdk $@
