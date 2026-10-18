#!/usr/bin/env python3

# Character transformation experiment

text = "HELLO"
result = ""

for char in text:
    if char.isupper():
        result += char.lower()
    else:
        result += char.upper()

print(result)
