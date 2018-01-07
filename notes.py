#!/usr/bin/env python

import os
import sys
import tempfile

from datetime import datetime


FILENAME = os.path.expanduser("~/.daily_log")


def log(txt):
    with open(FILENAME, "a+") as f:
        f.write("{}\n".format(datetime.now()))
        f.write(txt)
        f.write("\n")


def log_simple():
    log(" ".join(sys.argv[1:]))


def show():
    with open(FILENAME, "r+") as f:
        print(f.read())


def edit():
    editor = os.environ.get("EDITOR", "vi")
    f, name = tempfile.mkstemp()

    os.system("{} {}".format(editor, name))

    with os.fdopen(f) as f:
        contents = f.read()

    log(contents)


def usage():
    sys.stderr.write("usage: note [edit|show|args]\n")
    sys.stderr.write("\twhere 'edit' opens and editor of your choice,\n")
    sys.stderr.write("\twhere 'show' dump your notes, and\n")
    sys.stderr.write("\t      'args' get appended to the log file as is\n")
    sys.exit(1)


def notes():
    if not len(sys.argv) > 1: usage()

    if sys.argv[1] == "edit": edit()
    elif sys.argv[1] == "show": show()
    else: log_simple()


if __name__ == '__main__':
    notes()
