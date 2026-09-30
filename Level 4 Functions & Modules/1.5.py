#!usr/bin/env python3

try:
    # prompting the user to enter an ip
    user_ip=input("enter the ip address:")
    user_ip=user_ip.split(".") # Converting the string into a list to make the for loop work if each octet contain 3 or 2 numbers

    is_valid=bool() # Boolean variable to store if the ip is valid or not

    for n in range(0,4): # looping throw all the list (index 0,1,2,3)
        if int(user_ip[n])  in range(0,256): # if the number in any index is between 0 and 255 the value of boolean would be True
             is_valid=True
    # The loop would continue
        else:
            is_valid=False
            break # if we find any number that don't match the range the value of the boolean will be overwritten
            # ,and we break the loop immediately

    if is_valid:
        print(f"The ip {".".join(user_ip)} is valid")
    else:
        print(f"The ip {".".join(user_ip)} is not valid")
except Exception as e: # expecting any kind of errors
    print(f"an error occurred: {e}")