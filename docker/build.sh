#!/bin/bash

. docker/tools/build_python3.sh docker_demos $@
. docker/tools/build_python3.sh stream_demos $@
. docker/tools/build_python3.sh horovod_docker_demos $@
. docker/tools/build_python3.sh horovod_stream_demos $@
