# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.stream import Handler as h
from suanpan.stream import Stream
from suanpan.stream.arguments import String
import utils


class Demo(Stream):
    def afterInit(self):
        utils.hello()

    # 定义输入
    @h.input(String(key="inputData1", required=True))
    # 定义输出
    @h.output(String(key="outputData1"))
    def call(self, context):
        # 从 Context 中获取相关数据
        args = context.args
        # 查看上一节点发送的 args.inputData1 数据
        print(args.inputData1)

        # 自定义代码

        # 将 args.inputData1 作为输出发送给下一节点
        return args.inputData1


if __name__ == "__main__":
    Demo()
