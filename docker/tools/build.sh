#!/bin/bash

REGISTRY="registry-vpc.cn-shanghai.aliyuncs.com"
NAMESPACE="shuzhi"
IMAGE_URL="${REGISTRY}/${NAMESPACE}/$1"
IMAGE_VERSION="$3"

PYTHON_VERSION="$2"
PYTHON_MAJOR_VERSION="$(echo $2 | head -c 1)"

. tools/retry.sh 3 docker build \
-t ${IMAGE_URL}:${PYTHON_VERSION}-${IMAGE_VERSION} \
-t ${IMAGE_URL}:${PYTHON_VERSION} \
-t ${IMAGE_URL}:${PYTHON_MAJOR_VERSION}-${IMAGE_VERSION} \
-t ${IMAGE_URL}:${PYTHON_MAJOR_VERSION} \
-t ${IMAGE_URL}:latest \
. \
-f ./docker/$1/Dockerfile \
--build-arg PYTHON_VERSION=${PYTHON_VERSION} \
${@:4}

docker push ${IMAGE_URL}:${PYTHON_VERSION}-${IMAGE_VERSION}
docker push ${IMAGE_URL}:${PYTHON_VERSION}
docker push ${IMAGE_URL}:${PYTHON_MAJOR_VERSION}-${IMAGE_VERSION}
docker push ${IMAGE_URL}:${PYTHON_MAJOR_VERSION}
docker push ${IMAGE_URL}:latest
