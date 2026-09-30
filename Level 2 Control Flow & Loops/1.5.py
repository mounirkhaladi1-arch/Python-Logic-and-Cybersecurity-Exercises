#!/usr/bin/env python3

def check_prime(n):
    # Starting divisor
    i = 2

    # Prime numbers must be greater than 1
    if n <= 1:
        print(f"{n} is Not a prime number")
        return False

    # Loop through all numbers from 2 up to (but not including) n
    for i in range(i, n):
        # If n is divisible by any i, it's not prime
        if n % i == 0:
            print(f"{n} is not a prime number")
            return False

    # If the loop completes without finding a divisor, the number is prime
    print(f"{n} is a prime number")
    return True

# find all prime numbers from 1 to 100
for j in range(1, 101):
    check_prime(j)
