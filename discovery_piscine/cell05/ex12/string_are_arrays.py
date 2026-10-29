#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    text = sys.argv[1]
    z_count = 0
    
    for char in text:
        if char == 'z':
            z_count += 1
            
    if z_count > 0:
        print('z' * z_count)
    else:
        print("none")
else:
    print("none")