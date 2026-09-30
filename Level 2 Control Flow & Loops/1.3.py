#!/usr/bin/env python3

# Initialize the counter at 0
i = 0

# Loop until we reach the end of 4-digit possibilities (9999)
while i < 10000:
    # Handle single digits (1-9) - adds three leading zeros
    # Note: This currently skips 0 because of the 0 < i condition
    if 0 <= i < 10:
        print(f"000{i}")

    # Handle double digits (10-99) - adds two leading zeros
    elif 9 < i < 100:
        print(f"00{i}")

    # Handle triple digits (100-999) - adds one leading zero
    elif 99 < i < 1000:
        print(f"0{i}")

    # Handle four digits (1000-9999) - no zeros needed
    elif 999 < i < 10000:
        print(f"{i}")

    # Increment the counter to move to the next number and avoid infinite loop
    i += 1
