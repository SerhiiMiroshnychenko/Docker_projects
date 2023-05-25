import socket

# Використовуємо ім'я контейнера сервера
server_address_port = ("server", 20001)
buffer_size = 1024

# Create a UDP socket at client side
udp_client_socket = socket.socket(
    family=socket.AF_INET, type=socket.SOCK_DGRAM)

udp_client_socket.sendto(str.encode('Hello UDP Server!'), server_address_port)

while True:
    # Отримання введення від користувача
    msg_from_client = input('Please enter your message: ')
    if msg_from_client == 'exit':
        break
    bytes_to_send = str.encode(msg_from_client)

    # Send to server using created UDP socket
    udp_client_socket.sendto(bytes_to_send, server_address_port)

    msg_from_server = udp_client_socket.recvfrom(buffer_size)
    msg = msg_from_server[0].decode()
    print(f'Message from Server: "{msg}".')

udp_client_socket.close()
