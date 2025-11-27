#!/usr/bin/env python3

import sys

i = len(sys.argv)
print(f"parameters {i - 1}")

while (i > 1):
	print(f"{sys.argv[i - 1]}: {len(sys.argv[i - 1])}")
	i -= 1
