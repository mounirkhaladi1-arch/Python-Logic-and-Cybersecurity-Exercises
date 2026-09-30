#!/usr/bin/env python3

# We ask the user for the number and in the same time make sure it's integer

number= int(input("Enter a number: "))

# If the remainder of dividing this number by 2 is 0, it is even; otherwise, it is odd

if number % 2 == 0:  # We check if the number is even or odd using the modulo operator (%). If number % 2 == 0, it's even
    print("Even")
else:
    print("Odd")