#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
import sys
numbers = len(sys.argv) - 1
if numbers == 0:
	print("0 arguments.")
elif numbers == 1:
	print("1 argument:")
else:
	print("{} arguments:".format(numbers))
for n in range(numbers):
	print("{}: {}".format((n + 1), sys.argv[n + 1]))
