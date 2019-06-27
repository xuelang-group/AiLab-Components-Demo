# coding=utf-8
from __future__ import absolute_import, print_function

import argparse
import sys

import suanpan


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("component")
    args, rest = parser.parse_known_args()

    sys.argv = sys.argv[:1]
    return suanpan.run(args.component, rest)


if __name__ == "__main__":
    main()
