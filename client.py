from socket import * 
from serial import *

serverName= 'localhost' #Change to Azure server
serverPort=12000
clientSocket= socket(AF_INET, SOCK_DGRAM)

message=input()