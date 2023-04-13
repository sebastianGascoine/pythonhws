# File Name:     echo_server.py
# Programmer:    Sebastian Gascoine
# Date:          Dec. 5, 2022
#
import socket

host = '127.0.0.1'        # Symbolic name meaning all available interfaces
port = 3000      # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5) 
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    datflip = str(repr(data))
    datflip = datflip[-2:1:-1]

    if not data: break
    data = str.encode(datflip)
    conn.sendall(data)
conn.close()