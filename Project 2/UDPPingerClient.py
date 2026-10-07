# UDPPingerClient.py -- ECE 333 Project 2 client starter (Python 3)
# The handout gives no client code; this outline is the course's own starting point. Replace each
# "#Fill in start ... #Fill in end" with your code. The Project 2 notes explain every blank.
# Start UDPPingerServer.py in another terminal first, then run:   python3 UDPPingerClient.py

from socket import *
import sys
import time

serverName = sys.argv[1] if len(sys.argv) > 1 else 'localhost'  # the computer running the server
serverPort = 12000

#Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
#Wait at most one second for each reply
clientSocket.settimeout(1);

for sequence_number in range(1, 11):
    sendTime = time.time()
    message =  ("PING " + str(sequence_number) + " " + str(sendTime))
    start = time.perf_counter()  # a precise clock for the RTT on every OS
    #Send the message to the server
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    try:
        #Receive the reply
        receievedMessage = clientSocket.recv(1024).decode()
        rtt = time.perf_counter() - start 
        #Print the reply and the RTT in seconds
        print(receievedMessage, "\t", "RTT = ", f"{rtt:.6f}s")
    except timeout:
        print('Request timed out')

clientSocket.close()
