#!/usr/bin/env python3

import sys

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    text = sys.argv[2]
    
    count = text.count(keyword)
    
    if count > 0:
        print(count)
    else:
        print("none")
else:
    print("none")