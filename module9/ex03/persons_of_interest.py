#!/usr/bin/env python3

def famous_births(scientists):
	scientists = sorted(scientists, key=(lambda i: i["name"]))
	for person in scientists:
		name = scientists[person]["name"]
		age = scientists[person]["date_of_birth"]
		print("{name} is a great scientist born in {age}.")

scientists = {
	"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
	"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
	"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
	"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(scientists)
