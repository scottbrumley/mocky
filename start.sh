#!/bin/bash

if [[ $1 == 'dev' ]]
  then
    docker run -it -p 5000:5000 --name mocky-dev -v ${PWD}:/app -v /etc/localtime:/etc/localtime:ro -v /etc/timezone:/etc/timezone:ro mocky /bin/bash
else
    docker run -d --restart always --net host --name mocky -v /etc/localtime:/etc/localtime:ro -v /etc/timezone:/etc/timezone:ro mocky
fi

