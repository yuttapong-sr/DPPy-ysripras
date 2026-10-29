#!/usr/bin/env python3

import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    missing_length = 8 - len(s)
    print(s + 'Z' * missing_length)

if len(sys.argv) < 2:
    print("none")
else:
    for param in sys.argv[1:]:
        length = len(param)
        if length > 8:
            shrink(param)
        elif length < 8:
            enlarge(param)
        else:
            print(param)