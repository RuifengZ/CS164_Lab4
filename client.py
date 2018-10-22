# handling errors in python socket programs

import socket  # for sockets
import sys  # for exit

try:
    # create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit()

print('Socket Created')

host = 'www.google.com'
port = 80

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

print('IP address of ' + host + ' is ' + remote_ip)

# Connect to remote sever
s.connect((remote_ip, port))
print('Socket Connected to ' + host + ' on ip ' + remote_ip)

# Sending som data to the remote server
message = "GET / HTTP/1.1\r\n\r\n"

try:
    # Set the whole string
    s.sendall(message.encode())
except socket.error:
    # Send failed
    print('Send Failed')
    sys.exit()

print('Message sent successfully')
