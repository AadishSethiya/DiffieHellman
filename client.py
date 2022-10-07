import socket
from random import randint

def MillerRabin(n):
    #defining a function for miller rabin test

    if(n == 2):
        return True

    a = 1 + randint(1,n-1)      #initializing the base
    d = n -1
    
    while(d%2 == 0):
        d = d//2        #finding n-1 = 2^r*d
    
    res = 1
    
    for i in range(d):
        res = (res*(a%n))%n

    if res == 1:
        return True

    while d != n - 1:
        if res == n-1:
            return True
        for i in range(d):
            res = (res*(a%n))%n
        d = 2*d

    return False

def isPrime(n):
    #function to check if the number is prime
    if n<= 1 or n == 4:
        return False

    count = 0

    for i in range(n):
        if MillerRabin(n):
            count += 1
    
    if count >= n//2:
        return True

    return False

if __name__ == "__main__":

    client = socket.socket()        #starting the client socket

    client.connect(('localhost',9999))      #connecting to server socket

    print("Connected Successfully")

    while True:
        p = int(input("Enter the first prime number: "))    #taking user input for prime number
        if not isPrime(p):
            print("Invalid prime number, try again")
            continue
        break
    
    while True:
        g = int(input("Enter the generator: "))     #taking user input for generator
        if not g<p:
            print("Invalid generator, try again")
            continue
        break
    
    client.send(f"({p},{g})".encode())      #sending the prime and generator to the other user

    key = int(input("Enter the key: "))     #taking the user input fot key b

    code = (g**key)%p       #computing (g^b)%p

    client.send(f"{code}".encode())     #sending the code

    c_received = eval(client.recv(1024).decode())       #receiving the code from the other user

    encoded_msg = c_received**key%p     #computing (g^(ab))%p

    print(f"The secret key is: {encoded_msg}")