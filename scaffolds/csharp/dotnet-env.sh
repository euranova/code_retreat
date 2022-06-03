#!/bin/bash

ENABLE_TTY=${ENABLE_TTY:--t}

docker run -i ${ENABLE_TTY} --rm -v ${PWD}:/app -w /app mcr.microsoft.com/dotnet/sdk:3.1-alpine $@
