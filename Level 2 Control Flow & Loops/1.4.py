#!/usr/bin/env python3

# Prompt the user for input and convert the string into an integer
year = int(input("Enter a year: "))

# A leap year must be divisible by 400
# OR divisible by 4 while NOT being divisible by 100
# The 'and' operator takes precedence over 'or' in Python logic
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
else:
    # If the conditions above aren't met, it's a common year (365 days)
    print(f"{year} is not a leap year")
