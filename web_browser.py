import socket

HOST = "data.pr4e.org"
PORT = 80
DOC = "words.txt"

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
cmd = f'GET http://{HOST}/{DOC} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
mysock.close()
