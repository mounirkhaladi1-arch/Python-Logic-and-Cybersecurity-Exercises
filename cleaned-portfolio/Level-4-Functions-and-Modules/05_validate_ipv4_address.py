#!/usr/bin/env python3

# IPv4 validation exercise

import ipaddress

ip = input("Enter an IPv4 address: ")

try:
    ip_obj = ipaddress.ip_address(ip)
    if ip_obj.version == 4:
        print("Valid IPv4 address")
    else:
        print("Not a valid IPv4 address")
except ValueError:
    print("Not a valid IPv4 address")
