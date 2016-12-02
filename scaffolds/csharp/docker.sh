#!/bin/bash

docker run -it --rm -v $PWD:/app -w /app/src/CodeRetreat microsoft/dotnet:1.1-sdk-projectjson bash
