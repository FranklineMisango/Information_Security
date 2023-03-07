import socket

def portscanner(host, port, protocol="tcp"):
    """
    Scan a port on a given host using the specified protocol.

    Args:
    - host (str): The IP address or domain name of the host to scan.
    - port (int): The number of the port to scan.
    - protocol (str): The protocol to use for the scan, either "tcp" or "udp".
    """
    # Create a socket object for the specified protocol
    if protocol == "tcp":
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    elif protocol == "udp":
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    else:
        print("Error: Invalid protocol specified")
        return

    # Try to connect to the specified port on the host
    if s.connect_ex((host, port)):
        print("Port {} is closed".format(port))
    else:
        print("Port {} is open".format(port))

# Allow the user to specify the host and port to scan
host = input("Enter the host to scan: ")
port = int(input("Enter the port to scan: "))

# Allow the user to specify the protocol to use for the scan
protocol = input("Enter the protocol to use (tcp/udp): ")

# Scan the specified port on the host using the specified protocol
portscanner(host, port, protocol)
