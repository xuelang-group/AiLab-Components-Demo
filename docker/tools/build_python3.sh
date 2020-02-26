#!/bin/bash

for verion in {3.6,3.7}; do
    . docker/tools/build.sh $1 $verion $2 ${@:3}
done
