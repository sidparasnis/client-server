# UDP_Client

from socket import *
serverName = '127.0.0.1'
serverPort = 50069

clientSocket = socket(AF_INET, SOCK_DGRAM)

again = "Y"

while True:
    message = input("\nInput int,int,operation or 'quit' to quit: ")
    if message == 'quit':
        break
    print ("\n ")
    print ("-->> Sending: " + message)
    d = 0.1
    while d<2:
        try:
            clientSocket.settimeout(d)
            clientSocket.sendto(message.encode(), (serverName, serverPort))

            modifiedMessage, serverAddress =  clientSocket.recvfrom(2048)

            print ("<<-- At Client message received: " + modifiedMessage.decode() + "\n")
            clientSocket.settimeout(None)
            break;
        except timeout:
            print ('Resending...')
            d *= 2

print (" ")
print ("++++   Client Program Ends   ++++")
print (" ")

clientSocket.close()
