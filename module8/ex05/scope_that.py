#!/usr/bin/env python3

def add_one(i: int):
	i += 1
	print(f"funciton_variable {i}")

i = 3
print(f"main variable before {i}")
add_one(i)
print(f"main variable after {i}")

