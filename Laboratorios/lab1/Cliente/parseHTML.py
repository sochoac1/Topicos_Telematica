import socket
from bs4 import BeautifulSoup
import httpMethods
import constants  



def parseHtml(name_html, server):

    links =[]
    with open('Client/' + name_html) as fp:
        soup = BeautifulSoup(fp, "html.parser")
        images = soup.findAll('img') 
        print(images)
        css = soup.find_all('link')
        video = soup.find_all('video')
        for img in images:
            links.append(img['src'])
        for c in css:
            links.append(c['href'])
        for v in video:
            links.append(v['src']) 
    if len(links) > 0:
        print("**********************")
        for data_to_send in links:
            #Create new Client
            client_socket = clientParser(server)
            httpMethods.httpGet(client_socket, server, data_to_send)
            print("**********************")

def clientParser(server):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((server,constants.PORT))
    return client
