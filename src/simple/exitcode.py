#!/usr/bin/env python3
"""
Return an exit/status code.
"""

import sys                                #← for sys.argv & sys.exit.
import random                             #← for random.randrange().


def main (args):                          #← args from sys.argv.
    """
    Return command-line exit code, or random exit code.
    """
    exit_code = None
    if len(args) > 1:                     #← if command-line args…
        exit_code = toint(sys.argv[1])    #← convert 1st argument.
    if exit_code is None:
        exit_code = random.randrange(256) #← random int in [0…255].

    return exit_code                      #← passed to sys.exit().


def toint (val):
    """
    Convert string to int, return None if invalid.
    """
    try:
        result = int(val)
    except ValueError:
        result = None
    return result


if __name__ == '__main__':
    code = main(sys.argv)                 #← pass sys.argv to main.
    sys.exit(code)                        #← terminate & set code.

# vim: et ts=4 sw=4 sts=4 :
