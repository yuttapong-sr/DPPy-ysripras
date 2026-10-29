#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    target_param = sys.argv[1]

    user_input = input("What was the parameter? ")
    
    if user_input == target_param:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")