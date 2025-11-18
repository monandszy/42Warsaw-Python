#!/usr/bin/env python3
print("Give me a number: ", end='')
i = input()

try:
	int(i)
	print("This number is an integer")
except:
	print("This number is a decimal")	

