#!/usr/bin/env python3

import sys
import re

i = len(sys.argv)

if (i != 3):
	print("none")
	exit(1)
needle = sys.argv[1]
hay = sys.argv[2]

count = len(re.findall(needle, hay))
if (count > 0):
	print(f"{count}")
else:
	print("none")
