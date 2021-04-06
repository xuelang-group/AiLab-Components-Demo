#!/bin/bash

tags=$(git tag)
if [ -z "$tags" ]; then
    echo "0.0.1"
else
    git describe --abbrev=0 --tags master || git describe --abbrev=0 --tags origin/master
fi
