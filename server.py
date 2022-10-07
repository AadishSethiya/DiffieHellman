from ast import Str
import socket

server = socket.socket()        #staring the socket serer for user
print("Server started")

server.bind(('localhost',9999))     

server.listen(1)        
print("Waiting for client")

while True:
    client, address = server.accept()       #connecting to the client 
    print(f"Connected with {address}")

    p , g = eval(client.recv(1024).decode())        #receiving the prime number and generator from the client

    print(f"Received the prime number {p} and generator {g} successfully")

    key = int(input("Enter the key: "))     #taking user input for key a

    code = (g**key)%p       #computing (g^a)%p

    c_received = eval(client.recv(1024).decode())       #receiving the code from the client

    client.send(f"{code}".encode())     #sending the code to the client

    encoded_msg = c_received**key%p     #computing (g^(ab))%p

    print(f"The secret key is: {encoded_msg}")

    client.close()

    break