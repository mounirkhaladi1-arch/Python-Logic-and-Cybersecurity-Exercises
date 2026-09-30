#!/usr/bin/env python3


#10. Given a dictionary of usernames and passwords, print the password for a given username.

# Creating a dictionary of users & passwords
data_base={"admin": "P@ssw0rd123",
    "root": "toor",
    "user1": "guest",
    "john_doe": "secret123",
    "jane_doe": "password",
    "it_dept": "it_admin",
    "guest_acc": "welcome",
    "dev_user": "coding101",
    "security": "secure_pass",
    "test_user": "test1"
}

# Prompting the user to enter the username then the password
user=input("Enter your username: ")
password=input("Enter your password: ")

# check if the username giving by the user match the exact password in the dictionary
try:
    if data_base[user]==password:
     print("You are logged in")

except KeyError: # If it don't match we tell them that they are wrong and exit the program
    if user=="" and password=="":
        print("please enter your password and you're username")


    else:
        print("Wrong username or password")
