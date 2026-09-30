#!/usr/bin/env python3

newString = "H4ck3r"
b = 0
result = ""  # 1. Start with an empty string!

while b < len(newString):
    if b % 2 == 0:
        # 2. Append the uppercase letter to the result
        result += newString[b].upper()
    else:
        # 2. Append the lowercase letter to the result
        result += newString[b].lower()

    b += 1

print(f"The name is: {result}")

