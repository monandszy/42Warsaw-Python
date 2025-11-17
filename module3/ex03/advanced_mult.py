#!/usr/bin/env python3

i = 0
while(i <= 10):
	j = 0
	res = 0
	print(f"Table of {i}:", end='')
	while(j <= 10):
		print(f"{res} ", end='')
		res += i
		j += 1
	print("")
	i += 1

