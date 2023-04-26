#!/usr/bin/env python3
"""
Display script name and command-line arguments.
"""
import sys


def main (args):
    """
    Display all strings in `args` parameter. Number the
    arguments after the first, or if missing, do nothing.
    """
    print(f"Script: {args[0]}")
    for num, arg in enumerate(args[1:]):
        print(f"Arg #{num + 1}: {arg}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

# vim: et ts=4 sw=4 sts=4 :
