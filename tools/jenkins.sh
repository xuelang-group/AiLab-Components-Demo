#!/bin/bash

echo "Jenkins build started..."
curl -X GET http://xxx.xxx.xxx.xxx/job/my-comopnents/build?token=my-comopnents || echo "Jenkins configs error: tools/jenkins.sh"
