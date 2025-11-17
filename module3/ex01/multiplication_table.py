#!/usr/bin/env python3

print("Enter a number")
i = int(input())

j = 0;
while (j < 10):
	res = i * j
	print(f"{j} x {i} = {res}")
	j += 1
