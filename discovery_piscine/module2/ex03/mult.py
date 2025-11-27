#!/usr/bin/env python3

i1 = input("Enter the first number: ")
i2 = input("Enter the second number: ")

res = int(i1)*int(i2)
print(f"\n{i1} x {i2} = {res}")
if (res < 0):
    print("This number is negative.")
elif(res == 0):
    print("This number is both positive and negative")
else:
    print("This number is positive.")

