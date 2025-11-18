#!/usr/bin/env python3
origin = [2, 8, 9, 48, 8, 22, -12, 2]
print(origin)

new = origin.copy()
for num in origin:
	if (num < 5):
		new.remove(num)

print(new)
