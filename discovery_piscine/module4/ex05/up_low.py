#!/usr/bin/env python3

i = input("String: ")
for c in i:
	if (c >= 'a' and c <= 'z'):
		print(c.upper(), end = '')
	elif (c >= 'A' and c <= 'Z'):
		print(c.lower(), end = '')
	else:
		print(c, end = '')
print("")
