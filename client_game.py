# Name: Shimey Loo
# Date: 08/11/21
# Description: Programming Project 4 - Client - Game

# --------------------------------------
# Sources Used:
# James F. Kurose, Keith Ross, Computer Networking A Top Down Approach
# https://docs.python.org/3/library/socket.html
# Programming Project: Sockets and HTTP from Module 2
# Lecture Module 4 - Exploration: Socket Programming
# --------------------------------------

from socket import *

# The client creates a socket and connects to ‘localhost’ and port xxxx
serverName = "127.0.0.1"                            # host
serverPort = 1028                                   # port

clientSocket = socket(AF_INET, SOCK_STREAM)         # create socket object
clientSocket.connect((serverName, serverPort))      # connect client and server

# When connected, the client prompts for a message to send
print("Connected to: localhost on port:", serverPort)
print("""Hangman Instructions:
      Your goal is to guess the word. Fill in the blanks by guessing one letter at a time to see if it’s in the word.
      If you have guessed correctly, the letter will appear in the blank spaces. Select a letter not in the word, and 
      you will lose a life. You get 5 lives.""")

# Start game
message = input("Enter 'ready' to start the game: ")
message = message.lower()
while message != "ready":
    message = input("Enter 'ready' to start the game: ")
    message = message.lower()

clientSocket.send(message.encode())                 # Send to server that client is ready to start the game

possible_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
guess_list = []                                     # keeps track of the client's guesses

while True:
    data = clientSocket.recv(1024).decode()

    if int(data[0]) <= 0:                           # You lose when you have no more lives left
        print("")
        print("You have", data[0], "lives left.")
        print("Word:", data[1:])
        print("YOU LOST!")
        break

    completed_word = True
    for each_letter in data:
        if each_letter == "_":
            completed_word = False
    if completed_word:                              # You win when you guess the word correctly
        print("")
        print("Word:", data[1:])
        print("YOU WON!")
        break

    # print message for client
    print("")
    print("You have", data[0], "lives left.")
    print("Word:", data[1:])
    print("Letters you have entered:", guess_list)

    message = input("Enter letter: ")
    message = message.lower()

    invalid = True
    while invalid:                                  # Make sure inputs are valid
        if len(message) == 0:
            message = input("Invalid Input. Please try again: ")
            message = message.lower()
        elif message in guess_list:
            message = input("Letter has been already been guessed. Try again: ")
            message = message.lower()
        elif message not in possible_list:
            message = input("Invalid Input. Try again: ")
            message = message.lower()
        else:
            invalid = False

    # The client sends the message
    guess_list.append(message)
    clientSocket.send(message.encode())

# Sockets are closed (can use with in python3)
clientSocket.close()