#!/usr/bin/env python3

def famous_births(scientists):
	sort = sorted(scientists, key=(lambda i: i[1]))
	for person in sort:
		name = scientists[person]["name"]
		age = scientists[person]["date_of_birth"]
		print(f"{name} is a great scientist born in {age}.")

scientists = {
	"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
	"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
	"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
	"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(scientists)
