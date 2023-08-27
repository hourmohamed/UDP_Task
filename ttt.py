# SERVER
import socket
import io
def getline(filename,line_number):
    with open(filename,"r") as f:
        lines =f.readlines()
    for i, line in enumerate(lines ):
        if i ==line_number:
          return line
filename = "server.txt"
f=open (filename,"r")
host = socket.gethostbyname(socket.gethostname ())
socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_server .bind((host, 9090))

line = f.readlines()
num_lines=len(line)


#socket_server.sendto ("HELLO CLIENT".encode('utf-8'),(host,9090))
while True:
    # Receive a packet from the client.
    data, address = socket_server .recvfrom(1024)

    message = data.decode('utf-8')
    print (message)
    message_int =int (message)
    # Send a reply to the client.
    message_str=str(getline(filename,message_int))
    socket_server.sendto(message_str.encode('utf-8'),address)
    #socket_server .sendto(f"server sends to the client message number : {message} ".encode('utf-8'),address)
    f.close()