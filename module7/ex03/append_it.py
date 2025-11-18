#!/usr/bin/env python3

import sys

if (len(sys.argv) < 2):
	print("none")
	exit(1)

for s in sys.argv:
	if (s.find("ism", len(s) - 3) != -1):
		print(s)
