#!/usr/bin/env python

import argparse
import re

DEFAULT_VERSION_PARRTERN = r"__version__\s*=\s*\"(\d+)\.(\d+)\.(\d+)(?:-([\d\w\.]+))?\""
DEFAULT_VERSION_TEMPLATE = '__version__ = "{}"'
DEFAULT_VERSION_FILE = "version"


class Version(object):
    def __init__(self, major, minor, micro, pre=None):
        self.major = major
        self.minor = minor
        self.micro = micro
        self.pre = pre

    def __str__(self):
        version = ".".join(str(i) for i in [self.major, self.minor, self.micro])
        if self.pre:
            version = "-".join([version, self.pre])
        return version

    @classmethod
    def load(cls, file=DEFAULT_VERSION_FILE, pattern=DEFAULT_VERSION_PARRTERN):
        with open(file, "r") as verfile:
            major, minor, micro, pre = next(
                re.finditer(pattern, verfile.read())
            ).groups()
        return cls(int(major), int(minor), int(micro), pre)

    def save(
        self,
        file=DEFAULT_VERSION_FILE,
        pattern=DEFAULT_VERSION_PARRTERN,
        template=DEFAULT_VERSION_TEMPLATE,
    ):
        with open(file, "r+") as verfile:
            old = verfile.read()
            new = re.sub(pattern, template.format(self), old, count=1)
            verfile.seek(0)
            verfile.write(new)
            verfile.truncate()
        return file

    def update(self, major=None, minor=None, micro=None, pre=None):
        self.major = major if major is not None else self.major
        self.minor = minor if minor is not None else self.minor
        self.micro = micro if micro is not None else self.micro
        self.pre = pre if pre is not None else self.pre
        return self

    def upgrade(self, utype="micro", pre=None):
        mapping = {
            "major": self.upgrade_major,
            "minor": self.upgrade_minor,
            "micro": self.upgrade_micro,
        }
        return mapping[utype](pre=pre)

    def upgrade_major(self, pre=None):
        return self.update(major=self.major + 1, minor=0, micro=0, pre=pre)

    def upgrade_minor(self, pre=None):
        return self.update(minor=self.minor + 1, micro=0, pre=pre)

    def upgrade_micro(self, pre=None):
        return self.update(micro=self.micro + 1, pre=pre)


def get(file=DEFAULT_VERSION_FILE, pattern=DEFAULT_VERSION_PARRTERN):
    version = Version.load(file=file, pattern=pattern)
    print(version)
    return version


def upgrade(
    utype="micro",
    pre=None,
    file=DEFAULT_VERSION_FILE,
    pattern=DEFAULT_VERSION_PARRTERN,
    template=DEFAULT_VERSION_TEMPLATE,
):
    version = Version.load(file=file, pattern=pattern)
    version = version.upgrade(utype=utype, pre=pre)
    version.save(file=file, template=template)
    print("Upgrade:", version)
    return version


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["get", "upgrade"], default="get")
    parser.add_argument("-u", "--utype", default="micro")
    parser.add_argument("--pre")
    args = parser.parse_args()

    if args.action == "get":
        get()
    elif args.action == "upgrade":
        upgrade(utype=args.utype, pre=args.pre)
    else:
        raise Exception("No match action: {}".format(args.action))


if __name__ == "__main__":
    main()
