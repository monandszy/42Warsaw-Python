#!/usr/bin/env python3

import sys

if (len(sys.argv) != 3):
	print("none")
	exit(1)

try:
	i1 = int(sys.argv[1])
	i2 = int(sys.atgv[2])
	arr = range(i1, i2)
	print(arr)
except:
	print("Invalid arguments")
