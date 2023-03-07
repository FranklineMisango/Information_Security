#Importing the socket
import socket

#setting up the Transmission protocols as IPV6 
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 444

#Binding the client to the client socket
clientsocket.connect((host,port))

#The message that we receive from the servce should be equal to 1024 bytes
message = clientsocket.recv(1024)
#Close the socket and decode the Ascii message from server 
clientsocket.close()
print(message.decode('ascii'))
