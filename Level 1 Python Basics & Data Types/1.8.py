#!/usr/bin/env python3

# Instead of using built-in libraries, we use the mathematical definition of binary:
# Summing (bit * 2^n), where 'n' is the bit's position (index) starting from 0.
# We skip the calculation if the bit is 0, as it adds nothing to the total.

def encode_binary_to_decimal():
    result = 0
    num = 0b100101  # Input binary number
    position = 0

    while num > 0:
        # Extract the Least Significant Bit (LSB) using a bitwise AND mask
        bit = num & 1

        # Add (bit * 2^position) to our running total
        # If the bit is 0, this adds 0. If it's 1, it adds the power of 2.
        result += bit * pow(2, position)

        # Increment the power/position for the next iteration
        position += 1

        # Shift all bits to the right by 1 to process the next bit.
        # This eventually reduces 'num' to 0, terminating the loop.
        num >>= 1

    print(f"Decimal result: {result}")


# Calling the function
encode_binary_to_decimal()








