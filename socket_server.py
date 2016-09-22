import socket
import os

sock = socket.socket()
sock.bind(('localhost',8000))
sock.listen(1)
buffer_size = 2048

while True:
    connection, address = sock.accept()
    data = connection.recv(buffer_size)
    arr = data.split('\n')[0].split(' ')[1]
    path = './' + arr
    
    if not os.path.isfile(path):
        path ='./index.html'

    print(path)

    file = open(path, 'rb')
    connection.send("""HTTP/1.1 200 OK\nContent-Type: text/html\n\n\n""" + file.read())
    file.close()
    connection.close()
sock.close()