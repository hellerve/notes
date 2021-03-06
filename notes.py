#!/usr/bin/env python

import os
import re
import sys
import subprocess
import tempfile

from datetime import datetime

FILENAME = os.path.expanduser("~/.daily_log")


def read():
    with open(FILENAME, "r+") as f:
        return f.read()


def log(txt):
    with open(FILENAME, "a+") as f:
        f.write("{}\n".format(datetime.now()))
        f.write(txt)
        f.write("\n")


def log_simple():
    log("{}\n".format(" ".join(sys.argv[1:])))


def show():
    print(read())


def search(qs, ign):
    contents = read()
    query = re.compile(qs, re.MULTILINE | re.DOTALL | ign)

    offsets = query.search(contents)

    if not offsets:
        sys.stderr.write("Nothing found for {}\n".format(qs))
        exit(1)

    start = offsets.start()
    end = offsets.end()

    before = contents[:start]
    before = before[before.rindex("\n"):]
    after = contents[end:]
    after = after[:after.index("\n")]

    print("{}{}{}".format(before, contents[start:end], after))


def edit_subprocess(editor):
    f, name = tempfile.mkstemp()
    # Can't use the file descriptor provided by tempfile.mkstemp in subprocess
    # Thus, we close it and create a NEW file descriptor for use in subprocess.
    os.close(f)
    rv = subprocess.check_call([editor, name])
    with open(name, 'r') as f:
        contents = f.read()
    log(contents)
    os.remove(name)


def edit():
    editor = os.environ.get("EDITOR", "vi")
    edit_subprocess(editor)


def usage():
    sys.stderr.write("usage: note [edit|search|show|args]\n")
    sys.stderr.write("\twhere 'edit' opens an editor of your choice,\n")
    sys.stderr.write("\t      'search' queries your notes,\n")
    sys.stderr.write("\t      'isearch' queries your notes case-independently,\n")
    sys.stderr.write("\t      'show' dump your notes, and\n")
    sys.stderr.write("\t      'args' get appended to the log file as is\n")
    sys.exit(1)


def notes():
    if not len(sys.argv) > 1: usage()

    if sys.argv[1] == "edit": edit()
    elif sys.argv[1] == "show": show()
    elif sys.argv[1] == "search": search(" ".join(sys.argv[2:]), 0)
    elif sys.argv[1] == "isearch": search(" ".join(sys.argv[2:]), re.I)
    else: log_simple()


if __name__ == '__main__':
    notes()
