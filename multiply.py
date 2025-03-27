#!/usr/bin/env python3

import sys

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: multiply.py <number1> <number2>")
        sys.exit(1)

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        result = multiply(a, b)
        print(result)
    except ValueError:
        print("Error: Invalid number format")
        sys.exit(1)