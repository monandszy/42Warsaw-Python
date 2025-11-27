#!/usr/bin/env python3

def array_of_names(people):
	names = list()
	for human in people:
		names.append(f"{human.capitalize()} {people[human].capitalize()}")
	return(names)

people = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}

print(array_of_names(people))
