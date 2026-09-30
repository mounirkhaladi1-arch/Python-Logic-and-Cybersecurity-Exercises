#!/usr/bin/env python3


# we need  to turn all the vowels into *

vowels = "AEIOUYaeiouy"  # Include both cases
word = "P@ssw0rd"
new_word = ""

for char in word:
    if char in vowels:
        new_word += "*"
    else:
        new_word += char

print(new_word)  # Output: P@ssw0rd (Note: 'o' is a zero here)

