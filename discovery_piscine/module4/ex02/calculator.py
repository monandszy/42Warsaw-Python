#!/usr/bin/env python3
try:
	i1 = int(input("Give me the first number: "))
	i2 = int(input("Give me the second number: "))
except:
	print("Invalid Input")
	exit(1)
print("Thank you!")

print(f"{i1} + {i2} = {i1 + i2}")
print(f"{i1} - {i2} = {i1 - i2}")
print(f"{i1} / {i2} = {i1 / i2}")
print(f"{i1} * {i2} = {i1 * i2}")
