#!/usr/bin/env python3


# Creating a dictionary that include ports and there services

ports_services={    20: "FTP (Data Transfer)",
                    21: "FTP (Control)",
                    22: "SSH (Secure Shell)",
                    23: "Telnet",
                    25: "SMTP (Email)",
                    53:"DNS (Domain Name System)",
                    80: "HTTP (Web)",
                    110: "POP3 (Email Receiving)",
                    443: "HTTPS (Secure Web)",
                    3389: "RDP (Remote Desktop)",
                }

# Prompting the user to choose a specific port  or service


user_input=int(input("Enter a service (20,21,22,23,25,53,80,110,,443,3389): "))


if user_input in ports_services:
    print(f"the port {user_input} is: {ports_services.get(user_input)}")
else:
    print("enter a port number")
