#!/usr/bin/env python3

def find_the_redheads(people):
	return list(dict(filter(lambda person: person[1] == "red", people.items())).keys())

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))
