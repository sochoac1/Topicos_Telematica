
#---Method to obtain headers and build a response---#
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
    elif(my_file.endswith('.msi')):
        mimetype='application/msi'
    else:
        header='HTTP/1.1 404 File Not Found'.encode()
        return header        
    
    header='HTTP/1.1 200 OK\n'
    header += 'Content-Type: '+str(mimetype) + "\r\n\r\n"
    print('---------------- RESPONSE ----------------')
    print(header)
    print('<--The Status Line indicates--> ')
    print('HTTP/1.1: HTTP protocol to be used.')
    print('Status Code: An HTTP status code 200 means success.')
    print('<--Headers-->')
    print('Content-type: Refers to reusable collection of metadata for a category of content.')
    response = header.encode('utf-8')
    return response