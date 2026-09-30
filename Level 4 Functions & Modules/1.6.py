#!usr/bin/env python3
import random
import string

#importing all hex characters

hexchars=string.hexdigits

# we don't need lowercase characters so we delete them
# since the string is immutable we need to create new variable and replace them by nothing

new_hex_list=hexchars.replace("abcdef","")

#we put each pair together so it would b easier to join

mac_address=[str(random.choice(new_hex_list))+random.choice(new_hex_list) for _ in range(6)]
mac_address=":".join(mac_address) # separate each pair by a ':'

# We print the result
print(mac_address)


