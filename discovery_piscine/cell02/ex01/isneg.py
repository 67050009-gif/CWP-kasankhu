#!/usr/bin/env python3

number = input()

try:
    num = float(number)
    if num < 0:
        print("This number is negative.")
    elif num > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")
except ValueError:
    pass