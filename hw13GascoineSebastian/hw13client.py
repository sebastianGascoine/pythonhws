# File Name:     hw13project1.py
# Programmer:    Sebastian Gascoine
# Date:          Dec. 5, 2022
#
import socket

host = '127.0.0.1'    
port = 3000             # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(b'Hello, world')
data = s.recv(1024)
s.close()
print('Received', repr(data))