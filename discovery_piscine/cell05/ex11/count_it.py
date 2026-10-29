#!/usr/bin/env python3

import sys

num_params = len(sys.argv) - 1

if num_params == 0:
    print("none")
else:
    print(f"parameters: {num_params}")
    
    for param in sys.argv[1:]:
        print(f"{param}: {len(param)}")