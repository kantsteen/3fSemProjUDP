from socket import * 
from serial import *

UDP_IP = '255.255.255.255' #Change to Azure server
UDP_PORT = 12000
sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) #Enable broadcast

# Serielforbindelse til GPS
with Serial("/dev/ttyAMA0", baudrate = 9600, timeout = 1) as ser:
    print("Reads raw GPS data and sends via UDP...")
    while True:
        line = ser.readline().decode('ascii', errors = 'ignore').strip()
        if line.startswith('$GPRMC'):
            print("Sending:", line)
            sock.sendto(line.encode(), (UDP_IP, UDP_PORT)) 
