#!/usr/bin/env python3


# asks for a password and only allows access if it matches "s3cr3t"

password=input("enter a password ")

if  password=="s3cr3t":          # check if  the password is equal to  "s3cr3t"
    print("Access Granted")
else:
    print("Access Denied")
