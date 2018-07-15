FROM nginx:alpine

# ツールをインストール
RUN apk --no-cache update && \
    apk --no-cache upgrade && \
    apk --no-cache add \
    openssl

COPY ./etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf
