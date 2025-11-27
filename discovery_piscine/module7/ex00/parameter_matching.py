#!/usr/bin/env python3

import sys

if (len(sys.argv) != 2):
	print("Wrong amount of arguments")
	exit(1)

word = sys.argv[1]

attempt = input("What was the parameter?: ")

if (word == attempt):
	print("Good job!")
else:
	print("Nope, sorry...")
	
