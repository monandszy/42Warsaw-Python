#!/usr/bin/env python3
print("Give me a number: ", end='')
i = input()

if (float(int(i)) == float(i)):
	print("This number is an integer")
else:
	print("This number is a decimal")
