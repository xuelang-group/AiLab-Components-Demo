# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.stream import Handler as h
from suanpan.stream import Stream
from suanpan.stream.arguments import String


class DemoIn2Out1(Stream):
    @h.input(String(key="inputData1", required=True))
    @h.input(String(key="inputData2", required=True))
    @h.output(String(key="outputData1", required=True))
    def call(self, context):
        args = context.args
        return args.inputData1 + args.inputData2


if __name__ == "__main__":
    DemoIn2Out1().start()
