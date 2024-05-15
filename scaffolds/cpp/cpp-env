#!/usr/bin/env bash

ENABLE_TTY=${ENABLE_TTY:--t}

docker run -i ${ENABLE_TTY} --rm --user ${UID} -v "${PWD}":/app euranova/cxxtest:1.1 $@
