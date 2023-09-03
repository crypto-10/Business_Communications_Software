import socket
import sys
try:
    # create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # set up the address to bind the socket to
    local_addr = ('', 80) # set the IP address and port number

    # bind the socket to the address
    sock.bind(local_addr)

    # receive a message
    buffer_size = 1000000
    bytes_received, sender_addr = sock.recvfrom(buffer_size)

    # check if the message was received successfully
    if bytes_received == 0:
        print('Error receiving message')
    else:
        message = bytes_received.decode()
        print(f'Received {len(message)} bytes from {sender_addr[0]}')
        print(f'{message}')

    # close the socket
    sock.close()
except KeyboardInterrupt:
    sys.exit()
