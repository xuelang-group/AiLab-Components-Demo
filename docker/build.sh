#!/bin/bash

. docker/tools/build_python3.sh slim-demos $@
. docker/tools/build_python3.sh gpu-demos $@
. docker/tools/build_python3.sh horovod-demos $@
