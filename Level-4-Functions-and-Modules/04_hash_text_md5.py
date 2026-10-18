#!/usr/bin/env python3

import hashlib

# Hash a string using MD5
text = "Hello, world!"
hash_value = hashlib.md5(text.encode()).hexdigest()
print(hash_value)
