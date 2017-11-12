# UDP_Server
from socket import *
from random import random
er = float(input("\nInput an Error Rate From 0 - 1: "))
serverPort = 50069
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The UDP server is ready to receive\n")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    if random() > er:
        print ("-->> At Server receved message is: " + message.decode() + "\n")
        print ("  -->> clientAddress is: " , str(clientAddress[0]) + "/" + str(clientAddress[1]) )
        modifiedMessage = message.decode().split(',')
        try:
            a = int(modifiedMessage[0])
            b = int(modifiedMessage[1])
        except:
            ret = 'Invalid Integers'
        op = modifiedMessage[2]
        if op == '+':
            ret = int(a)+int(b)
        elif op == '-':
            ret = int(a) - int(b)
            print (ret)
        elif op == '/':
            ret = int(a)/int(b)
        elif op == '*':
            ret = int(a)*int(b)
        else:
            ret = 'Invalid Operand'
        print ("<<-- At Server modified message to send back: '" + str(ret) + "'\n")
        serverSocket.sendto(str(ret).encode(), clientAddress)
    else:
        print ('Packet dropped.')
