#!/usr/bin/env python3

import sys

i = len(sys.argv)

if (i > 1):
	while(i > 1):
		print(sys.argv[i - 1])
		i -= 1	
else:
	print("none")
