#!/usr/bin/env python3
from dataclasses import replace

# Goal: Convert a list into a comma-separated string

# Define the list with mixed data types (integers, strings, booleans)
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "hello", True]

# Convert the entire list object into its literal string representation
mylist = str(mylist)

# Print the string and confirm its type
print(mylist)
print(type(mylist))

# Iterate through every single character in the string representation
for i in mylist:
    # Ensure current character is a string
    i = str(i)

    # Remove unwanted list formatting characters (spaces and brackets)
    i = i.replace(" ", "")
    i = i.replace("[", "")
    i = i.replace("]", "")
    i = i.replace("'", "")

    # Print characters horizontally without newlines
    print(i, end="", sep=",")

