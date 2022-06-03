#!/usr/bin/env bash

cd "$(dirname $0)" || exit 1

export ENABLE_TTY=" "

function run_test() {
  local folder=$1

  cd ${folder} || exit 1
  echo "[${folder}]"

  for script in build test; do
    if [ ! -f ./scripts/${script} ]; then
      echo -e "\t\tERROR: file not found: ${folder}/scripts/${script}"
    else
      if ./scripts/${script} > /dev/null 2>&1; then
        echo -e "\t\t${script} OK"
      else
        echo -e "\t\t${script} FAILED"
      fi
    fi
  done
}

export -f run_test

find . -maxdepth 1 -mindepth 1 -type d -print0 | xargs -0 -i bash -c "run_test {}"
