from parseHTML import *


def httpGet(client_socket, server, data_to_send):

    #---Sending the HTTP Request---#
    request = 'GET' + ' ' + data_to_send + ' ' + 'HTTP/1.1\r\nHost: ' + server + '\r\n\r\n'
    print('---------------- REQUEST ----------------')
    print(request.split('\r\n\r\n')[0])
    client_socket.send(request.encode())                #sends data on the socket with descriptor socket.

    #---Receiving the HTTP response---#
    actual=b's'                                         #This variable receives the response from the server. The default value can be any character in order to start looping.
    res = b''                                           #Inside the loop below, res updates it value until it receives an empty response, which means that the response is received successfully.
    while(True):                                        #Start looping until the client receives the complete response.    
        actual = client_socket.recv(9999999)
        if(actual == b''):
            break 
        else:
            res += actual

    response = res.split(b"\r\n\r\n")                   #Split the HTTP response  status line and headers between the body
    print('---------------- RESPONSE ----------------')
    print(response[0].decode()) 

    #---Copying the HTTP response file---#
    status_code = response[0].decode().split(' ')[1]    #Get the status code (e.g. HTTP/1.1 200 OK) Manage 200 or 404 status code
    if(status_code == '200'):
        file_receive = response[1]
        if(data_to_send.lstrip('/') == ('')):
            data_to_send ='html/index.html'
        elif(data_to_send[0] == '/'):
            data_to_send = data_to_send.lstrip('/')
        file = open("./Client/"+data_to_send, 'wb')
        file.write(file_receive)
        file.close() 

        
        client_socket.close()                           #Closing Socket connection  

        #---Parsing the HTTP response in case of being an HTML file---#
        if(data_to_send.endswith('.html')):
            name_html = data_to_send.lstrip('/')
            parseHtml(name_html, server)                #Method parseHtml
        
    else:
        print(response[1].decode())                     #Print error 404 (file not found)
    #Create a new socket
    return
            
def httpHead(client_socket, server, data_to_send):
    #---Send HEAD---
    request = 'HEAD' + ' ' + data_to_send + ' ' + 'HTTP/1.1\r\nHost: ' + server + '\r\n\r\n'
    print('---------------- REQUEST ----------------')
    print(request.split('\r\n\r\n')[0])
    client_socket.send(request.encode())
    #---Receive HEAD--
    data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)      
    print('---------------- RESPONSE ----------------')
    print(data_received.decode(constants.ENCONDING_FORMAT))     
    print("**********************")
    client_socket.close()