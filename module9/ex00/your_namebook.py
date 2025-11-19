#!/usr/bin/env python3

def array_of_names(people):
	print(list(people.items()))

people = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}

print(array_of_names(people))
