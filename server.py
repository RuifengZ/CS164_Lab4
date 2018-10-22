import socket
import sys

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 2163  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Created')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code: ' + str(msg[0]) + 'Message ' + msg[1])
    sys.exit()

print('Socket bind complete')

s.listen(10)
print('Socket now listening')

# wait to accept connection
conn, addr = s.accept()

# display client information
print('Connected with ' + addr[0] + ':' + str(addr[1]))

# keep talking with client
data = conn.recv(1024)
conn.sendall(data)

conn.close()
s.close()
