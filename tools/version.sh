#!/bin/bash

git describe --abbrev=0 --tags master || git describe --abbrev=0 --tags origin/master
