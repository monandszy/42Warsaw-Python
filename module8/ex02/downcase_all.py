#!/usr/bin/env python3

import sys

def lowcase_it(s) -> str:
	return (s.lower())

i = 1
while(i < len(sys.argv)):
	print(lowcase_it(sys.argv[i]))
	i += 1
