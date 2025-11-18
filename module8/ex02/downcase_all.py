#!/usr/bin/env python3

import sys

def lowcase_it(s) -> str:
	return (s.lowcase())

i = len(sys.argv)
while(i > 1):
	print(low_case_it(sys.argv[i -1]))
	i -= 1
