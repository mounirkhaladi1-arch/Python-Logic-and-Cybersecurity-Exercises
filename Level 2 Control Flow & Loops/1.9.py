#!/usr/bin/env python3

# Define the correct password for comparison
true_password = "s3cr3t"

# Start an infinite loop to keep asking until the correct password is provided
while True:
    # Prompt the user to enter their password
    password = input("enter your password: ")

    # Check if the entered password matches the stored true password
    if password == true_password:
        # Exit the loop immediately if the password is correct
        break
    else:
        # Inform the user and continue the loop if the password is incorrect
        print("passwords do not match")

# Print success message once the loop is broken
print("password is correct")
