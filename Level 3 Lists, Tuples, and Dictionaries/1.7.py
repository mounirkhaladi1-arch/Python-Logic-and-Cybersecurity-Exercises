#!/usr/bin/env python3

# Function to remove duplicates from a list.


def duplicate_remover(list_a):
    list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]

    result = []

    # Loop through the list using an index range
    for i in range(len(list_a)):
        # Set k to the last index of the list
        k = len(list_a) - 1

        # Start a while loop to compare the current element with others
        while i <= k:
            # Check if the current element matches the element at index k
            if list_a[i] == list_a[k]:
                # If they match but are at different positions, it's a duplicate
                if i != k:
                    break
                # If it's the same position, it's the unique occurrence
                else:
                    result.append(list_a[i])
                    break

            # Decrement k to check the next element from the right
            k -= 1

    # Print the original list
    print(list_a)
    # Print the list with duplicates removed
    print(result)

# testing the function

duplicate_remover(list_a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 9,4,5])