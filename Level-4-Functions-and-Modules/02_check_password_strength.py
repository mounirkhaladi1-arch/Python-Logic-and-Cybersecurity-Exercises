#!/usr/bin/env python3

# Check password strength

def password_strength(password):
    if len(password) < 8:
        return "weak"
    elif len(password) < 12:
        return "medium"
    else:
        return "strong"

password = input("Enter your password: ")
print(password_strength(password))
