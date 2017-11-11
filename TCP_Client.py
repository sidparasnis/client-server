# UDP_Client

from socket import *
serverName = '127.0.0.1'
serverPort = 50069

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
again = "Y"

while (again=="y") | (again=="Y"):
    message = input("\nInput int,int,operation: ")
    print ("\n ")
    print ("-->> Sending: " + message + "\n")

    clientSocket.send(message.encode())

    modifiedMessage =  clientSocket.recv(1024)

    print ("<<-- At Client message received: " + modifiedMessage.decode() + "\n")
    again = input("Do you want to repeat? (y or Y; anything else is a NO!)")

print (" ")
print ("++++   Client Program Ends   ++++")
print (" ")

clientSocket.close()
