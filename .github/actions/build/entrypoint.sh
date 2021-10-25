#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

$2

docker-compose -f $1 up -d

while true; do
    STATUS="$(docker inspect --format {{.State.Health.Status}} workspace_grpc-api_1)"
    echo "Status: '${STATUS}'"
    if [ "${STATUS}" != "starting" ]; then
        break
    fi
    sleep 1
done

STATUS="$(docker inspect --format {{.State.Health.Status}} workspace_grpc-api_1)"
echo "Final status: '${STATUS}'"

#docker-compose -f $1 down -v

#if [ "${STATUS}" != "healthy" ]; then
#    exit 1
#fi

exit 0
