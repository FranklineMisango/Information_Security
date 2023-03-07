import socket

# function to validate IP address
def validate_ip_address(ip_address):
    try:
        socket.inet_pton(socket.AF_INET, ip_address)
        return True
    except:
        return False

# function to validate port number
def validate_port(port):
    try:
        port = int(port)
        if port > 0 and port <= 65535:
            return True
        else:
            return False
    except:
        return False

# Socket initialization
s = socket.socket()

# Getting user input for IP address and port number
while True:
    ip_address = input("Please Enter Your IP address : ")
    if validate_ip_address(ip_address):
        break
    else:
        print("Invalid IP address. Please try again.")

while True:
    port = input("Please enter the port : ")
    if validate_port(port):
        break
    else:
        print("Invalid port number. Please try again.")

# Connecting to the server
s.connect((ip_address, int(port)))

# Receiving data from the server
data = s.recv(1024).decode('utf-8')

# Printing the received data
print(data)

# Closing the socket
s.close()
