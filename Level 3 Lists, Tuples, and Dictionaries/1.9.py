#!/usr/bin/env python3
from typing import Any

# 9. Find the longest word in a list.

# A list with words of varying lengths (2 to 12 characters)
word_list = [
    "it",
    "cat",
    "code",
    "flask",
    "python",
    "hacker",
    "network",
    "security",
    "algorithm",
    "development",
    "architecture"
]

# Initialize a list to store the length of each word
number_list = []

# Loop through each word to calculate its length
for word in word_list:
    # Append the integer length to our number_list
    number_list.append(len(word))

# Identify the highest number in the length list
max_len = max(number_list)

# Loop again to find which word(s) match that maximum length
for word in word_list:
    if len(word) == max_len:
        # Print the word that matches the target length
        print(f"{word} is the maximum length of {max_len}")
