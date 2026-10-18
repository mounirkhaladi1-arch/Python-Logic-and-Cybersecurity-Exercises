#!/usr/bin/env python3

# We define a list of words
words = ["cybersecurity", "python", "analysis", "network", "hacker"]

# We iterate through the words to find the longest one
longest_word = words[0]

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(f"The longest word is: {longest_word}")
