#!/bin/bash

CURRENT_VERSION=`. tools/version.sh`

MAJOR=`echo ${CURRENT_VERSION} | cut -f 1 -d "."`
MINOR=`echo ${CURRENT_VERSION} | cut -f 2 -d "."`
MICRO=`echo ${CURRENT_VERSION} | cut -f 3 -d "."`

case $1 in
    major)
        ((MAJOR+=1))
        MINOR=0
        MICRO=0
        ;;
    minor)
        ((MINOR+=1))
        MICRO=0
        ;;
    *)
        ((MICRO+=1))
        ;;
esac

UPGRADE_VERSION="${MAJOR}.${MINOR}.${MICRO}"

. tools/publish.sh ${CURRENT_VERSION} ${UPGRADE_VERSION}
. tools/jenkins.sh || echo "Jenkins configs error: tools/jenkins.sh"
