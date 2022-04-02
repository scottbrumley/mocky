#!/bin/bash

if [ $1 == 'dev' ]
  then
    docker image build -f Dockerfile-Dev -t mocky .
else
    docker image build -t mocky .
fi