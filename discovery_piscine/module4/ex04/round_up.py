#!/usr/bin/env python3

i = input("Give me a number: ")

try:
	i = int(i)
	print(f"{i}")
except:
	try:
		i = float(i)
		print(f"{int(i) + 1}")
	except:
		print("Not a number")

