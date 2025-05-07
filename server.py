from socket import *
from datetime import datetime, timedelta
import requests

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverAddress = ('', serverPort)

serverSocket.bind(serverAddress)
print("The server is ready")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    # print("Received message:" + message.decode())
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

            timestamp = dt_utc.isoformat() + "Z"


            # converting to CEST
            dt_cest = dt_utc + timedelta(hours=2)
            timestamp = dt_cest.isoformat() + "Z"


            lat_deg = int(parts[3][0:2])
            lat_min = float(parts[3][2:7])
            latitude = lat_deg + lat_min / 60.0
            if parts[4] == 'S':
                latitude *= -1

            lon_deg = int(parts[5][0:3])
            lon_min = float(parts[5][3:])
            longitude = lon_deg + lon_min / 60.0
            if parts[6] == 'W':
                longitude *= -1

            speed_knots = float(parts[7])

            return {
                'timestamp': timestamp,
                'latitude': latitude,
                'longitude': longitude,
                'speed_knots': speed_knots,
            }


        except Exception as e:
            print('Error while parsing', e)
            return None

    
    serverSocket.sendto(parse_gprmc(modifiedMessage.encode()), clientAddress)

    


