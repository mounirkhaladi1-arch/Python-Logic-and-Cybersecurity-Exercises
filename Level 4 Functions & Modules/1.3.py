#!/usr/bin/env python3
import random
import string

# Preparing all characters in both upper and lower case

strong_password=string.ascii_letters

# Making 12 random choices from the characters string and add them to another variable

password=random.choices(string.ascii_letters, k=12)

# The result would be a string so we need to join them with join()

password="".join(password)

print(f"the password is: {password}")