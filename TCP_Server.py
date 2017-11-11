# UDP_Server

from socket import *
serverPort = 50069
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ("The TCP server is ready to receive\n")
while True:

    connectionSocket, clientAddress = serverSocket.accept()
    message = connectionSocket.recv(1024)
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
    connectionSocket.sendto(str(ret).encode(), clientAddress)
    connectionSocket.close()
