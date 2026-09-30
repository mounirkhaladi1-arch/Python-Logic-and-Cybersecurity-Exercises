#!/usr/bin/env python3


def check_strong_password():
    password = input("enter your password: ")

    # Check for a number using a loop
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break

    # Final check: Length + Special Char (not alnum) + Number
    if len(password) >= 8 and not password.isalnum() and has_number:
        print("Password is strong")
        return True
    else:
        print("Password is weak")
        return False

check_strong_password()