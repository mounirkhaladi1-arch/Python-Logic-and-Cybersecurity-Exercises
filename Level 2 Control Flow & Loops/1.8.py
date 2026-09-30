#!/usr/bin/env python3

# Iterate through numbers from 1 to 100
for i in range(1, 101):

    # Check if the number is a multiple of both 3 and 5 (divisible by 15)

    if i % 15 == 0:
        print("FizzBuzz")

    # Check if the number is a multiple of 3

    elif i % 3 == 0:
        print("Fizz")

    # Check if the number is a multiple of 5

    elif i % 5 == 0:
        print("Buzz")

    # If not divisible by 3 or 5, print the number itself

    else:
        print(i)
