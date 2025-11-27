#!/usr/bin/env python3
i = input("Give me a number: ")

try:
	int(i)
	print("This number is an integer")
except:
	try:
		float(i)
		print("This number is a decimal")	
	except:
		print("Not a number...")

