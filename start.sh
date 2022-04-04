#!/bin/bash

if [[ $1 == 'dev' ]]
  then
    docker run -d -p 5000:5000 --name mocky-dev -v ${PWD}:/app -v /etc/localtime:/etc/localtime:ro -v /etc/timezone:/etc/timezone:ro mocky-dev
else
    docker run -d -p 5000:5000 --restart always --name mocky -v /etc/localtime:/etc/localtime:ro -v /etc/timezone:/etc/timezone:ro mocky
fi

