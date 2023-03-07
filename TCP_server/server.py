#Imports the socket module
import socket

#Setting up our serve name that will use the IPV4 connection stream, and TCP transmission protol
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Our host from a remote connection -> client.py [IP address] which is my linux IP
host = socket.gethostbyname()
#Listening port, can be changed to any other free port especially 4444
port = 444

#Binding out server to the host and port and setting maximum device connection to 3
serversocket.bind((host, port))
serversocket.listen(3)

#Condition to check that as long as there is a binding connection, the server will run otherwise it will close 
#Server closes after there is 3 connections
while True:
    clientsocket , address = serversocket.accept()
    print("Received connection from"%str(address))
    message = 'Thank you for connecting to the server' + '\r\n'
    clientsocket.send(message)
    clientsocket.close()
