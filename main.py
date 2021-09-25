# httpclient
# Exampel of how to program a simpel http client in python
# Ib Helmer Nielsen, UCN
import socket
host = "www.google.dk"
port = 80
# Create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the client to the webserver
client.connect((host,port))
# Send a http GET request, has to be as a bytestring
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
# Receive response from webserver
response = client.recv(4096)
print(response.decode())
client.close()
