from socket import * 
import serial

serverName= '255.255.255.255' #Change to Azure server
serverPort=12000
sock= socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) #Enable broadcast

# Serielforbindelse til GPS
with serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1) as ser:
    print("Reads raw GPS data and sends over UDP...")
    while True:
        line = ser.readline().decode('ascii', errors='ignore').strip()
        if line.startswith('$'):  # Tjek om det er en NMEA-sætning
            print("Sender:", line)
            sock.sendto(line.encode(), (UDP_IP, UDP_PORT))
