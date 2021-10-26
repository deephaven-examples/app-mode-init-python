#!/bin/sh

docker build --tag deephaven-examples/validate-tables /github-actions-validate/
$4

docker-compose -f $3 -p $5 up -d
TABLE_NAMES=$1 HOST=$2 docker-compose -f /github-actions-validate/docker-compose.yml -p $5 up --exit-code-from validate-tables
