FROM nginx:1.18.0-alpine
LABEL maintainer="YangSen <yangsen@cloud-star.com.cn>"

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
apk update && apk add --no-cache bash tini \
    && rm -rf /tmp/* /var/tmp/* /var/cache/apk/* \
    && rm -rf /root/.cache .build-deps
