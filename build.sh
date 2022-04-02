#!/bin/bash

if [[ $1 == 'dev' ]]
  then
    echo "Building Development Mocky Container"
    docker image build -f Dockerfile-Dev -t mocky .
else
    ehco "Building Production Mocky Container"
    docker image build -t mocky .
fi