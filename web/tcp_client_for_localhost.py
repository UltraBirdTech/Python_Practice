import socket

target_host = '127.0.0.1'
target_port = 9999

# crate socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # connect to server
    client.connect((target_host, target_port))
except ConnectionRefusedError as err:
    print('[ERROR]: ' + str(err))
    print('HOST: ' + str(target_host))
    print('PORT: ' + str(target_port))
    print('上記のホスト、ポートへのコネクションが確立できませんでした')
    exit()


# send data
client.send(b"ABCDEFG")

# recieve data
response = client.recv(4096)

print(response)
