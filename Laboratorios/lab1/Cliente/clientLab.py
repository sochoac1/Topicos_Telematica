import socket
import constants  
from httpMethods import *


def main():
    client_execution()

#Function to start client process...
def client_execution():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #The arguments passed to socket() are constants used to specify the address family(IPv4) and socket type(TCP).
    print('---------------- NEW CLIENT ----------------')
    print('Client is running...')
    server=input('Input the hostname: ')
    client_socket.connect((server,constants.PORT))                   #Connect the socket to the defined host and port
    local_tuple = client_socket.getsockname()                        #It returns the address to the socket that has been bound. 
    print('Connected to the server from:', local_tuple)
    print('Enter \"QUIT\" to exit')
    print('Input commands:')
    command_to_send = input()

    while command_to_send != constants.QUIT:
        if command_to_send == '':
            print('Please input a valid command...')
            command_to_send = input()  
        elif(command_to_send == constants.GET):
            data_to_send = input('Input data to GET: ')
            httpGet(client_socket, server, data_to_send)            #Calls the function which perform the GET method 
            main()
        elif(command_to_send == constants.HEAD):
            data_to_send = input('Input data to HEAD: ')
            httpHead(client_socket, server, data_to_send)           #Calls the function which perform the HEAD method 
            main()
        else:
            command_to_send = input('Invalid command, try again: ')
    #--QUIT--#
    request = command_to_send + ' ' + 'server' + ' ' + 'HTTP/1.1\r\nHost: ' + server + '\r\n\r\n'
    client_socket.send(request.encode())
    data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)        
    print(data_received.decode(constants.ENCONDING_FORMAT))
    print('Closing connection...BYE BYE...')
    client_socket.close() 
    main()

if __name__ == '__main__':
    main()