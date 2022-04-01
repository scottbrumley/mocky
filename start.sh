#!/bin/bash

docker run -d --restart always --net host --name mocky -v /etc/localtime:/etc/localtime:ro -v /etc/timezone:/etc/timezone:ro mocky
