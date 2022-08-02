# ********************************************************************************************
    # Lab: Introduction to sockets
    # Course: Topicos de Telemática
    # MultiThread TCP-SocketServer
# ********************************************************************************************

# Import libraries for networking communication and concurrency...

import socket
import threading
from httpMethods import *
import constants


# Defining a socket object...
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = constants.IP_SERVER

def main():
    print("***********************************")
    print("Server is running...")
    print("Dir IP:",server_address )
    print("Port:", constants.PORT)
    server_execution()

#Function to start server process...
def server_execution():
    tuple_connection = (server_address,constants.PORT)
    server_socket.bind(tuple_connection)                                                                                #Python's socket class assigns an IP address and a port number to a socket instance
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)                                                 #Provides an application program with the means to control socket behavior
    print ('Socket is bind to address and port...')
    server_socket.listen(5)                                                                                             #This denotes maximum number of connections that can be queued for this socket by the operating system.
    print('Socket is listening...')
    while True:
        client_connection, client_address = server_socket.accept()                                                      #Accepts an incoming connection request from a TCP client
        client_thread = threading.Thread(target=handler_client_connection, args=(client_connection,client_address))     #It allows you to manage concurrent threads(tasks, function calls) doing work at the same time.
        client_thread.start()                                                                                           #Call the start() method of the Thread class to start the thread. 
    
# Handler for manage incomming clients conections...
def handler_client_connection(client_connection,client_address):
    print(f'New incomming connection is coming from: {client_address[0]}:{client_address[1]}')
    is_connected = True
    while is_connected:
        request = client_connection.recv(4098260).split(b"\r\n\r\n")                                                     #Method and file_name b"GET /cover.jpg HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n"
        message = request[0].decode().split(' ')                                                                         #Split the request to get the method and the file name to obtain
        method = message[0] 
        file_name = message[1]
        print('---------------- REQUEST ----------------')
        print(method, file_name, ' HTTP/1.1/ ')

        #GET
        if (method == constants.GET):
            getMethod(client_connection, file_name)
            is_connected = False
        #HEAD
        elif(method== constants.HEAD):
            headMethod(client_connection, file_name)
            is_connected = False
        #QUIT
        elif (method == constants.QUIT and file_name=="server"):
            response = '200 BYE\n'
            client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
            is_connected = False
        else:
            response = '400 BCMD\n\rmethod-Description: Bad method\n\r'
            client_connection.sendall(response.encode(constants.ENCONDING_FORMAT))
    
    print(f'Now, client {client_address[0]}:{client_address[1]} is disconnected...')
    client_connection.close()

                                                                                    
if __name__ == "__main__":
    main()