# coding=utf-8
from __future__ import absolute_import, print_function

from suanpan.stream import Handler as h
from suanpan.stream import Stream
from suanpan.stream.arguments import String


class DemoIn1Out1(Stream):
    @h.input(String(key="inputData1", required=True))
    def call(self, context):
        pass


if __name__ == "__main__":
    DemoIn1Out1().start()
