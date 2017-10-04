#!/bin/bash

if [[ $# -eq 0 ]] ; then
    echo 'You need to provide a command as argument [php|phpspec|composer].'
    exit 0
fi

if [[ $1 == phpspec || $1 == test ]] ; then
    set -- "php ./vendor/phpspec/phpspec/bin/phpspec" "${@:2}"
fi

docker run --rm -it -v $PWD:/app -u $(id -u):$(id -g) composer $@
