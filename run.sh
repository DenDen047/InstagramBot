#!/bin/bash

NAME="main"

# 環境変数を設定
export MI_DATA_PATH=$1

# buildして、command実行
cd docker && \
docker-compose up --build

# コンテナを削除
docker rm docker_${NAME}_1
