#!/usr/bin/env python3

import sys

def expand(s) -> str:
	return(s + "zzzzzzzz")

def shrink(s) -> str:
	return(s[0:7])

argv = len(sys.argv)
i = 1
while(i < argv):
	s = argv[i]
	l = len(s)
	if (l < 8):
		print(expand(s))
	elif(l > 8):
		print(shrink(s))
	else:
		print(s)
	i += 1
