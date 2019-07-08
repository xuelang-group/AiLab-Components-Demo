# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.stream import Handler as h
from suanpan.stream import Stream
from suanpan.stream.arguments import String


class DemoIn1Out2Send2nd(Stream):
    @h.input(String(key="inputData1", required=True))
    @h.output(String(key="outputData1", required=True))
    @h.output(String(key="outputData2", required=True))
    def call(self, context):
        args = context.args
        self.send({"outputData2": args.inputData1})


if __name__ == "__main__":
    DemoIn1Out2Send2nd().start()
