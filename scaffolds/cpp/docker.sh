#!/usr/bin/env bash

docker run --user ${UID} -it -v ${PWD}:/app euranova/cxxtest
