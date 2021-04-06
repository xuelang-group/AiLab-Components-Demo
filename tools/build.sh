#!/bin/bash

ARCH="amd64"

REGISTRY="registry-vpc.cn-shanghai.aliyuncs.com"
NAMESPACE="shuzhi-${ARCH}"
IMAGE_NAME=$1
IMAGE_URL="${REGISTRY}/${NAMESPACE}/${IMAGE_NAME}"
PYTHON_VERSION="3.7"

. tools/retry.sh 3 docker build \
-t ${IMAGE_URL}:latest \
. \
-f ./docker/Dockerfile \
--build-arg PYTHON_VERSION=${PYTHON_VERSION} \
${@:2}

docker push ${IMAGE_URL}:latest