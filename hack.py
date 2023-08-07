import socket

target = "https://www.sliit.lk"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((target, 80))

http_request = "GET / HTTP/1.1\r\nHost: " + target + "\r\n\r\n"
s.send(http_request.encode())

result = s.recv(4096).decode()

print(result)

s.close()







