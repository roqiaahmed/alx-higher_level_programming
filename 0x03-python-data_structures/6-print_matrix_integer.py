#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
	for row in matrix:
	    for cul in row:
	        print("{:d}".format(cul), end=" "if cul != row[-1] else "")
	    print()
