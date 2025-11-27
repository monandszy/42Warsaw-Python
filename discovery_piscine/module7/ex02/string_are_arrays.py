#!/usr/bin/env python3

import sys

if (len(sys.argv) != 2):
	print("Invalid arguments")
	exit(1)

flag = True

for c in sys.argv[1]:
	if (c == 'z'):
		flag = False
		print('z', end='')

if (flag):
	print("none")
else:
	print("")

