#!/usr/bin/env python3

number = int(input("Enter a number\n"))

i = 0

while i <= 9:
    result = i * number
    print(f"{i} x {number} = {result}")
    i += 1