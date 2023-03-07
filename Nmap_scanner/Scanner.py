import nmap
import re
import os

# Define a regular expression for matching IP addresses
ip_regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"

#Customizing the scanner to look for all the open ports
scanner = nmap.PortScanner()
print("Welcome to our custom NMAP scanner")
print("<--------------------------------->")

# Loop until a valid IP address is entered
while True:
    ip_address = input("Please enter the IP address you want to scan: ")
    if re.match(ip_regex, ip_address):
        break
    else:
        print("Invalid IP address. Please try again.")

print("The IP address entered is:", ip_address)

# Check if script is being run with root privileges
if os.geteuid() != 0:
    print("This script requires root privileges to run nmap scans.")
    print("Please run this script with sudo.")
    exit()

# Prompt user to select type of scan
response = input("""Please select the type of scan you want to run:
                    1) SYN ACK Scan
                    2) UDP scan
                    3) Comprehensive Scan\n""")
print("You have selected option:", response)

#Checking whether the IP is running or not and alerting the user'

if int(response) == 1:
    print("Nmap Version ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    if 'tcp' in scanner[ip_address]:
        print("Open ports : ", list(scanner[ip_address]['tcp'].keys()))
    else:
        print("No TCP ports found open on this host.")
elif int(response) == 2:
    if int(response) == 1:
        print("Nmap Version ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    if 'udp' in scanner[ip_address]:
        print("Open ports : ", list(scanner[ip_address]['udp'].keys()))
    else:
        print("No UDP ports found open on this host.")
elif int(response) == 3:
    if int(response) == 1:
        print("Nmap Version ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    if 'tcp' in scanner[ip_address]:
        print("Open ports : ", list(scanner[ip_address]['tcp'].keys()))
    else:
        print("No open ports found open on this host.")
else :
    print("Sorry , we dont support that option yet")
    