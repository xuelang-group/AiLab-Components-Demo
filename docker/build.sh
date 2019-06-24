#!/bin/bash

# Slim

# Build Docker Code Server Images
. docker/tools/build_python3.sh docker_notebook $@

# Build Docker Code Server Images
. docker/tools/build_python3.sh docker_code_server $@

# Build Stream Code Server Images
. docker/tools/build_python3.sh stream_code_server $@

# Horovod

# Build Horovod Docker Notebook Images
. docker/tools/build_python3.sh horovod_docker_notebook $@

# Build Horovod Docker Code Server Images
. docker/tools/build_python3.sh horovod_docker_code_server $@

# Build Horovod Stream Code Server Images
. docker/tools/build_python3.sh horovod_stream_code_server $@
