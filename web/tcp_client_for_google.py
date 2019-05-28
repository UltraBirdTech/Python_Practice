import socket

target_host = 'google.co.jp'
target_port = 80

# crate socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # connect to server
    client.connect((target_host, target_port))
except ConnectionRefusedError as err:
    print('[ERROR]: ' + str(err))
    exit()

# send data
client.send(b"GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n")

# recieve data
response = client.recv(4096)

print(response)
