# Name: Shimey Loo
# Date: 08/11/21
# Description: Programming Project 4 - Server - Game

# --------------------------------------
# Sources Used:
# James F. Kurose, Keith Ross, Computer Networking A Top Down Approach
# https://docs.python.org/3/library/socket.html
# Programming Project: Sockets and HTTP from Module 2
# Lecture Module 4 - Exploration: Socket Programming
# --------------------------------------

from socket import *
from hangman import *

# The server creates a socket and binds to ‘localhost’ and port xxxx
localhost = "127.0.0.1"
serverPort = 1028

serverSocket = socket(AF_INET, SOCK_STREAM)            # create TCP welcoming socket
serverSocket.bind(('', serverPort))

# The server then listens for a connection
serverSocket.listen(1)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
connectionSocket, addr = serverSocket.accept()         # creates connection socket for new incoming client requests

# When connected, the server calls recv to receive data
print("Server listening on: localhost on port:", serverPort)
print("Connected by", addr)
print("Waiting for game to start...")
data = connectionSocket.recv(serverPort).decode()
print("From client:", data)

game = Hangman()                                       # Create a game of hangman
print("Answer:", game.get_word())
message = str(game.get_lives())
for space in game.get_guess():
    message = message + str(space)

connectionSocket.send(message.encode())                # send message to client that they connected

while True:
    data = connectionSocket.recv(serverPort).decode()

    if len(data) == 0:                                 # Connection ended by client
        print("Connection ended by client.")
        break

    game.submit_guess(data)                            # Update hangman game with new guess

    # The server prints the data, then prompts for a reply
    print("Front client:", data)
    message = str(game.get_lives())
    for space in game.get_guess():
        message = message + str(space)

    # the server sends the reply
    connectionSocket.send(message.encode())            # send message to client that they connected

# Sockets are closed (can use with in python3)
connectionSocket.close()
