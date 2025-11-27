#!/usr/bin/env python3

def greetings(name = 0):
	if (isinstance(name, str)):
		print(f"Welcome, {name}!")
	else:
		print(f"{name} is not a name")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
