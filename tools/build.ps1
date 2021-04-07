$ARCH = "amd64"

$REGISTRY ="registry.cn-shanghai.aliyuncs.com"
$NAMESPACE = "shuzhi-${ARCH}"
$IMAGE_NAME = $args
$IMAGE_URL = "${REGISTRY}/${NAMESPACE}/${IMAGE_NAME}"
$PYTHON_VERSION = "3.7"

docker build -t ${IMAGE_URL}:latest . -f .\docker\Dockerfile
docker push ${IMAGE_URL}:latest
