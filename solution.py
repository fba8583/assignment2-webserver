# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket
    serverSocket.bind(("127.0.0.1", port))
    # Fill in start
    serverSocket.listen(1)
    # Fill in end
    # connectionSocket, addr = serverSocket.accept() #Fill in start      #Fill in end

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()  # Fill in start      #Fill in end
        # try:

        try:
            message = connectionSocket.recv(1024).decode("utf-8")  # Fill in start    #Fill in end
            # print(message)
            # print(message.split())

            filename = message.split()[1][1:]
            # print(filename)

            f = open(filename)
            # f = open('/helloworld.html')
            outputdata = f.read()  # Fill in start     #Fill in end
            print(outputdata)

            # Send one HTTP header line into socket.
            # Fill in start

            # Fill in end

            # Send the content of the requested file to the client
            # for i in range(0, len(outputdata)):
            # connectionSocket.send(outputdata[i].encode())

            # connectionSocket.send("\r\n".encode())
            # connectionSocket.close()
        except IOError:
            # Send response message for file not found (404)
            # Fill in start

            # Fill in end

            # Close client socket
            # Fill in start

            # Fill in end

            # except (ConnectionResetError, BrokenPipeError):
            # pass

            serverSocket.close()


# sys.exit()  # Terminate the program after sending the corresponding data

def main():
    webServer(13331)


if __name__ == '__main__':
    main()
