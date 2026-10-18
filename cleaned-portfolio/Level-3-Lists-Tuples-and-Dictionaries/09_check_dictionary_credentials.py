#!/usr/bin/env python3

# Define a dictionary of known users and passwords
users = {
    "admin": "s3cr3t",
    "alice": "letmein",
    "bob": "password123"
}

# Prompt for a username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the username exists and if the password matches
if username in users and password == users[username]:
    print("Access granted")
else:
    print("Incorrect username or password")
