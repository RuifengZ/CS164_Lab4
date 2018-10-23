import socket
import sys
from _thread import *
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


# keep talking with client

def clientthread(conn):
    conn.send('Welcome to the server. Type something and hit enter\n'.encode())
    reply = "".encode()
    while True:
        data = conn.recv(1024)
        if "\n".encode() in data:
            if '!q'.encode() == reply.strip():
                break
            print(reply[:9])
            if reply[:9] == '!sendall '.encode():
                reply = 'OK... '.encode() + reply[9:] + '\n'.encode()
                conn.sendall(reply)
            reply = "".encode()
        else:
            reply += data
        if not data:
            break
    conn.close()


while 1:
    # wait to accept connection and display client information
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    # start new thread takes 1st argument as a function name to be run
    # second is the tuple of arguments to the function.
    start_new_thread(clientthread, (conn,))

s.close()

