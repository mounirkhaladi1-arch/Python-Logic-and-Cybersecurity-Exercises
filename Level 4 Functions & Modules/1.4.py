#!usr/bin/env python3
import hashlib


# Prompting the user for a string

user_string=input("Enter your string: ")
# Hashing the string and convert it to hex
hashed_string=hashlib.md5(user_string.encode()).hexdigest()

# printing the result

print(hashed_string)