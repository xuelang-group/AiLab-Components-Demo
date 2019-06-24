# coding=utf-8
from __future__ import absolute_import, print_function

import argparse
import importlib
import sys


def load(name):
    try:
        module_name, component_name = name.rsplit(".", 1)
        module = importlib.import_module(module_name)
        return getattr(module, component_name)
    except Exception as e:
        print("Load component error!", file=sys.stderr, flush=True)
        raise e


def run(name):
    return load(name)()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("Run")
    args = parser.parse_args()

    run(args.component)
