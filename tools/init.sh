#!/bin/bash

set -e

PROJECT_NAME=${SUANPAN_PROJECT_NAME:-"my-comopnents"}
GIT_REMOTE_ORIGIN=${SUANPAN_PROJECT_GIT_REMOTE_ORIGIN}

git clone --depth 1 https://github.com/yamajik/AiLab-Components-Demo ${PROJECT_NAME}
cd ${PROJECT_NAME}
rm -rf .git tools/init.sh tools/release-oss.sh
mv docker/my-components docker/${PROJECT_NAME}
sed -i "" "s/my-comopnents/${PROJECT_NAME}/g" tools/jenkins.sh || sed -i "s/my-comopnents/${PROJECT_NAME}/g" tools/jenkins.sh
sed -i "" "s/my-comopnents/${PROJECT_NAME}/g" README.md || sed -i "s/my-comopnents/${PROJECT_NAME}/g" README.md

echo 'version = "0.0.0"' > components/__init__.py
git init && git add . && git commit -m "init" && git tag "0.0.0"
git flow init -d
if [ -n "${GIT_REMOTE_ORIGIN}" ]; then
    git remote add origin ${GIT_REMOTE_ORIGIN}
    git push -u --all && git push --tags
fi
echo "${PROJECT_NAME} init finished!"
