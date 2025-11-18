#!/usr/bin/env python3

i = input("Give me a number: ")

try:
	int(i)
	print(f"{int(i)}")
except:
    print(f"{int(float(i)) + 1}")

