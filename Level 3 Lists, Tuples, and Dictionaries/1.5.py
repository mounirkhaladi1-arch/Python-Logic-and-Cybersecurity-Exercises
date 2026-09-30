#!/usr/bin/env python3
import random       # importing the random library


#  creating a random number list

j=random.randint(2,10)
numbers=[i for i in range(1,j)]    # we create a non-empty list randomly

random.shuffle(numbers) # we shuffle the list

print(numbers)   # We print the shuffled  list (to compare it with the ordered one)
t=0
m=0

while t<len(numbers) :      # We defin a loop  that pass all the numbers is the list

    for m in range(len(numbers)):       # We make a for loop to compare that number t to all the numbers
        if numbers[t] < numbers[m]:
            numbers[t],numbers[m]=numbers[m],numbers[t]     # if the number in the index t is smaller
                                                            # we swap it with the number in index m




    t+=1
    m+=1


print(numbers)



