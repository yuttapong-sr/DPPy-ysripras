#!/usr/bin/env python3

def add_one(n):
    n += 1
    return n

my_var = 5

print(f"Before calling the method: {my_var}")

my_var = add_one(my_var)

print(f"After calling the method: {my_var}")