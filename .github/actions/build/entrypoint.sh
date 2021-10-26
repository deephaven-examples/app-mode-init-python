#!/bin/sh

$2
docker-compose -f $1 -p $3 up -d
