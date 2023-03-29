
#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
HOST = '' # empty string means bind to all available interfaces
PORT = 8080 # use non-privileged port number
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve at will...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]

        #Open the requested file
        f = open(filename[1:])

        #Read the content of the file and generate an HTTP response message
        outputdata = f.read()
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + outputdata

        #Send the HTTP response header and file content to the client
        connectionSocket.send(response.encode())

        #Close the client socket
        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(response.encode())

        #Close the client socket
        connectionSocket.close()

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
