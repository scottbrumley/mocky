#!/bin/bash

if [[ $1 == 'dev' ]]
  then
    docker container stop mocky-dev
    docker system prune
else
    docker container stop mocky
    docker system prune
fi