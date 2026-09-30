#!/usr/bin/env python3

def login(real_username, real_password):
    # Loop from 1 to 3
    for i in range(1, 4):
        user = input("Enter your username: ")
        passw = input("Enter your password: ")

        # Check if credentials match
        if user == real_username and passw == real_password:
            print("Login Successful")
            return True

        # If credentials fail, check if we have tries left
        else:
            tries_left = 3 - i
            if tries_left > 0:
                print(f"Wrong! You still have {tries_left} tries left.")
            else:
                print("Access Denied: No tries left.")
                return False
    return False


login("admin","s3cr3t")



