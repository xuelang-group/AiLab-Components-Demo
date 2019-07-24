# coding=utf-8
from __future__ import absolute_import, print_function

import suanpan
import utils
from suanpan.docker import DockerComponent as dc
from suanpan.docker.arguments import Folder


# 定义输入
@dc.input(Folder(key="inputData1", alias="inputFolder", required=True))
@dc.param(key="param1", alias="p", default=1)
# 定义输出
@dc.output(Folder(key="outputData1", alias="outputFolder", required=True))
def Demo(context):
    # 从 Context 中获取相关数据
    args = context.args
    # 查看上一节点发送的 args.inputData1 数据
    print(args.inputFolder)
    print(args.p)

    # 自定义代码
    utils.hello()

    # 将 args.outputData1 作为输出发送给下一节点
    return args.outputFolder


if __name__ == "__main__":
    suanpan.run(Demo)
