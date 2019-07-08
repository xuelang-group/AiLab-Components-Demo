# coding=utf-8
from __future__ import absolute_import, print_function

import time

from suanpan.stream import Handler as h
from suanpan.stream import Trigger
from suanpan.stream.arguments import String


class TriggerDemo(Trigger):
    def loop(self):
        for i in range(100):
            yield i
            time.sleep(1)

    @h.output(String(key="outputData1"))
    def call(self, context, data):  # pylint: disable=unused-argument
        print(data)


if __name__ == "__main__":
    TriggerDemo().start()
