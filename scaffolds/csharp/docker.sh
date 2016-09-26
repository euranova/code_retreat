#!/bin/bash

docker run --rm -v $PWD:/app -w /app microsoft/dotnet:1.0.0-preview2-sdk $@
