#!/usr/bin/env python3

import random


def guess_num():
    """
    A simple number guessing game where the user has 3 attempts
    to guess a random number between 1 and 20.
    """

    print("You need to guess a number between 1 and 20.")
    print("you have 3 tries!!")

    # Create a list of numbers from 1 to 20
    numbers = []
    for x in range(1, 21):
        numbers.append(x)

    # Randomly select the winning number from the list
    lucky_number = random.choice(numbers)

    # Loop for a maximum of 3 attempts
    for i in range(1, 4):

        # Get user input and convert it to an integer
        guess = int(input("Enter your guess: "))

        # Check if the guess matches the lucky number
        if guess == lucky_number:
            print("You guessed the number")
            return True
        else:
            # Calculate and display remaining attempts
            tries_left = 3 - i
            if tries_left > 0:
                print(f"Wrong! You still have {tries_left} tries left.")
            else:
                # End of game if no tries remain
                print("You lost the game")
                return False  # Exit immediately after losing all tries

    return False


# Execute the game function
guess_num()
