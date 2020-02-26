#!/bin/bash

set -e

# curl -sfL "https://suanpan-public.oss-cn-shanghai.aliyuncs.com/suanpan/components/python/project/init.sh" | sh -
ossutil cp tools/init.sh "oss://suanpan-public/suanpan/components/python/project/init.sh" -f
