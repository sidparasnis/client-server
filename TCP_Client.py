# UDP_Client

from socket import *
serverName = '127.0.0.1'
serverPort = 50069

again = "Y"

while True:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    message = input("\nInput int,int,operation or 'quit' to quit: ")
    if message == 'quit':
        break
    print ("\n ")
    print ("-->> Sending: " + message + "\n")

    clientSocket.send(message.encode())

    modifiedMessage =  clientSocket.recv(1024)

    print ("<<-- At Client message received: " + modifiedMessage.decode() + "\n")

clientSocket.close()
print (" ")
print ("++++   Client Program Ends   ++++")
print (" ")
