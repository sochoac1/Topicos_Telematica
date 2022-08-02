from fileinput import filename
import constants
from getHeader import *
from fileExistence import *



#---GET METHOD --#
def getMethod(client_connection, file_name):
    file_name = file_name.lstrip('/')                                                                            #Remove the first slash
    if(file_name == ''):
        file_name= 'index.html'
    file_name = constants.DOCUMENT_ROOT +file_name
    if not(checkFileExistance(file_name)):
        #print('<-------File not found----->')
        header = 'HTTP/1.1 404 Not Found\r\n\r\n'.encode() 
        response = '<html><body>Error 404: File not found</body></html>'.encode('utf-8')                                      
    else:
        file=open(file_name,'rb')
        response=file.read()
        file.close() 
        header = getHeader(file_name)                
    final_response = header + response
    client_connection.sendall(final_response) 
    print('---------------- SENDING ... ----------------')

#---HEAD METHOD---#
def headMethod(client_connection, file_name):
    file_name = file_name.lstrip('/')
    print('Archivo sin:', file_name)
    if(file_name == ''):
        file_name= 'index.html'
    file_name = './Server/'+file_name
    if not (checkFileExistance(file_name)):
        #print('<-------File not found----->')
        header = 'HTTP/1.1 404 Not Found\r\n\r\n'.encode() 
    else:
        header=getHeader(file_name)
    header = header.rstrip(b'\r\n\r\n')
    client_connection.sendall(header)
    print('**********************')