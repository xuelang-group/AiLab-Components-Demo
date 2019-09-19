#!/bin/bash

set -e

VERSION=`python tools/version.py get`

echo "Build Version: ${VERSION}"
. docker/build.sh ${VERSION} $@
