#!/bin/bash

set -e

VERSION=`. tools/version.sh`

. docker/build.sh ${VERSION} $@
