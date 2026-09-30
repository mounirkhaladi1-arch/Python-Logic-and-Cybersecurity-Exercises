#!/usr/bin/env python3


# prompt the user for a word

word=input("enter word: ")

# set the variables that allow us to identify if the word is palindrome or not

i=0
j=len(word)-1
is_palindrome=bool()

while i<j: # this allows to stop in the middle of the word and avoid any intersections between 'i' and 'j'
    if word[i]!=word[j]: # checking by trying to negate the word if any letter don't match with  his opposite so it's not palindrome
        is_palindrome=False
        break
    else:
        is_palindrome=True
        break
i+=1
j-=1


if is_palindrome:
    print("palindrome")
else:
    print("not palindrome")