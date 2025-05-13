# from socket import * 
# from serial import *

# UDP_IP = '255.255.255.255' #Change to Azure server
# UDP_PORT = 12000
# sock = socket(AF_INET, SOCK_DGRAM)
# sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) #Enable broadcast

# # Serielforbindelse til GPS
# with Serial("/dev/ttyAMA0", baudrate = 9600, timeout = 1) as ser:
#     print("Reads raw GPS data and sends via UDP...")
#     while True:
#         line = ser.readline().decode('ascii', errors = 'ignore').strip()
#         if line.startswith('$GPRMC'):
#             print("Sending:", line)
#             sock.sendto(line.encode(), (UDP_IP, UDP_PORT)) 


from socket import *
import time

# Test string to send
testString = "$GPRMC,121525.000,A,5537.8451,N,01204.6738,E,0.16,317.18,050525,,,A*63"

# Server configuration
UDP_IP = '255.255.255.255'  # For local testing, you might want to use your server's IP instead
UDP_PORT = 5000

# Create UDP socket
sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)  # Enable broadcast

# Send the test string
print("Sending:", testString)
sock.sendto(testString.encode(), (UDP_IP, UDP_PORT))

# Optional: Send multiple messages with delay
"""
for i in range(5):
    print(f"Sending message {i+1}:", testString)
    sock.sendto(testString.encode(), (UDP_IP, UDP_PORT))
    time.sleep(2)  # Wait 2 seconds between messages
"""

sock.close()
print("Test string sent successfully!")