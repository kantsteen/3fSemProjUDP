from socket import *
from datetime import datetime, timedelta

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverAddress = ('', serverPort)

serverSocket.bind(serverAddress)
print("The server is ready")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Received message:" + message.decode())
    modifiedMessage = message.decode().upper()

    def parse_gprmc(modifiedMessage):
        parts = modifiedMessage.split(',')
        if parts[2] != 'A':
            print('Void data')
            return None
        
        # date, time, lat, long
        try:
            raw_time=parts[1]
            raw_date=parts[9]

            dt_utc = datetime.strptime(raw_date + raw_time[:6], "%d%m%y%H%M%S") # check %d if 'day' in datetime doesn't work

            # converting to CEST
            dt_cest = dt_utc + timedelta(hours=2)
            timestamp = dt_cest.strftime("%Y-%m-%d %H:%H:%S") # check %d if 'day' in datetime doesn't work



        except Exception as e:
            print('Error while parsing', e)
            return None

        


    
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)


