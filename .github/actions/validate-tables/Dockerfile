FROM docker/compose:alpine-1.29.2

COPY --chmod=0xyz entrypoint.sh /entrypoint.sh
COPY validate /github-actions-validate

ENTRYPOINT ["/entrypoint.sh"]
