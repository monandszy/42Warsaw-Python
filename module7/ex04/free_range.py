#!/usr/bin/env python3

import sys

if (len(sys.argv) != 3):
	print("none")
	exit(1)

try:
	i1 = int(sys.argv[1])
	i2 = int(sys.argv[2])
	if (i1 > i2):
		r = range(i2, i1)
	else:
		r = range(i1, i2)
	print(list(r))
except:
	print("Invalid arguments")
