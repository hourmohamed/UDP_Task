# SERVER
import socket
host = socket.gethostbyname(socket.gethostname ())
socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_server .bind((host, 2025))


while True:
    # Receive a packet from the client.
    data, address = socket_server .recvfrom(1024)
    message = data.decode('utf-8')
    print (message)
    # Send a reply to the client.
    socket_server .sendto(f"server sends to the client message number : {message} ".encode('utf-8'),address)
    
