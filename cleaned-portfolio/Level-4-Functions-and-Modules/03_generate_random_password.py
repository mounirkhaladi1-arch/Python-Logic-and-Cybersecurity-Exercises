#!/usr/bin/env python3

import random
import string

# Generate a random password with letters only

def generate_password(length=12):
    characters = string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(length))

print(generate_password())
