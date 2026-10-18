#!/usr/bin/env python3

import random

# Generate a fake MAC address in the format XX:XX:XX:XX:XX:XX

def generate_mac():
    return ":".join(f"{random.randint(0, 255):02x}" for _ in range(6))

print(generate_mac())
