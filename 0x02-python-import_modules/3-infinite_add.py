#!/usr/bin/python3
import sys
sum_num = 0
for n in range(1, len(sys.argv)):
	sum_num += int(sys.argv[n])
print("{}".format(sum_num))
