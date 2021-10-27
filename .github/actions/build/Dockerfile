FROM docker/compose:alpine-1.29.2

COPY entrypoint.sh /entrypoint.sh

RUN ["chmod", "+x" ,"/entrypoint.sh"]

ENTRYPOINT ["/entrypoint.sh"]
