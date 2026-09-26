#!/usr/bin/python3
"""Print numbers from 1 to N, replacing multiples of 3, 5, and 15."""
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} n".format(sys.argv[0]))
        sys.exit(1)

    n = int(sys.argv[1])
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    print(" ".join(result))
