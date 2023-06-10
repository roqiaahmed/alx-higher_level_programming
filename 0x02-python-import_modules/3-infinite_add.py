#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
import sys
sum_num = 0
for n in range(1, len(sys.argv)):
	sum_num += int(sys.argv[n])
print("{}".format(sum_num))
