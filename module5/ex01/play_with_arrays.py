#!/usr/bin/env python3
origin = [2, 8, 9, 48, 8, 22, -12, 2]
print(origin)
new = origin.copy()
for i in range(len(new)):
    new[i] += 2
print(new)
