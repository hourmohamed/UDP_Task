#CLIENT
import socket
counter =str(0)
temp_counter=0
host = socket.gethostbyname(socket.gethostname ())
socket_client= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#socket_client.sendto ("HELLO SERVER".encode('utf-8'),(host,9090))
#print (socket_client.recvfrom (1024)[0].decode ('utf-8'))
while True:
    socket_client.sendto (counter.encode('utf-8'),(host,9090))
    counter = int(temp_counter)
    temp_counter+=1
    counter=str(counter)
    print (socket_client.recvfrom (1024)[0].decode ('utf-8'))
    
