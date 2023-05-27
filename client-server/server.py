import socket

# localhost 0.0.0.0, 127.0.0.1
HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    connection, address = s.accept()
    while connection:
        print(f'Connected with {address}')
        while True:
            data = connection.recv(1024)
            answer = data.upper()
            connection.sendall(answer)
            if answer == 'EXIT':
                break
