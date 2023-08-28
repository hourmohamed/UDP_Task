#CLIENT
import socket
counter =str(0)
temp_counter=0
host = socket.gethostbyname(socket.gethostname ())
socket_client= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
filename = "server.txt"
f=open (filename,"r")
line = f.readlines()
num_lines=len(line)
while True:
    if temp_counter>num_lines:
        break
    
    counter = int(temp_counter)
    temp_counter+=1
    counter=str(counter)
    socket_client.sendto (counter.encode('utf-8'),(host,9090))
    print (socket_client.recvfrom (1024)[0].decode ('utf-8'))
