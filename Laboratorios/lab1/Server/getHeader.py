
#---Method to obtain headers and build a response---
def getHeader(my_file):
    if(my_file.endswith('.jpg')):       #Identify file extensions
        mimetype='image/jpg'
    elif(my_file.endswith('.css')):
        mimetype='text/css'
    elif(my_file.endswith('.pdf')):
        mimetype='aplication/pdf'
    elif(my_file.endswith('.html')):
        mimetype='text/html'
    elif(my_file.endswith('.mp4')):
        mimetype='video/mp4'
    else:
        header='HTTP/1.1 404 File Not Found'.encode()
        return header        
    
    header='HTTP/1.1 200 OK\n'
    header += 'Content-Type: '+str(mimetype) + "\r\n\r\n"
    print('---------------- RESPONSE ----------------')
    print(header)
    response = header.encode('utf-8')
    return response