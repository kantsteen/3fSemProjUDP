from socket import *
from datetime import datetime, timedelta
import json
import requests

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverAddress = ('', serverPort)

#testString1 =  { "id": 3, "timestamp": "2025-05-08T10:18:00Z", "latitude": 55.6775, "longitude": 12.5681, "speedKnots": 0.16}



serverSocket.bind(serverAddress)
print("The server is ready")

message, clientAddress = serverSocket.recvfrom(2048)
print("Received message:" + message.decode())
messageDecoded = message.decode()

    # testString = "$GPRMC,121525.000,A,5537.8451,N,01204.6738,E,0.16,317.18,050525,,,A*63"
   


def parse_gprmc(messageDecoded):
    parts = messageDecoded.split(',')
    if parts[2] != 'A':
            print('Void data, no satellite fix')
            return None
        
        # date, time, lat, long
    try:
        raw_time=parts[1]
        raw_date=parts[9]

        dt_utc = datetime.strptime(raw_date + raw_time[:6], "%d%m%y%H%M%S") # check %d if 'day' in datetime doesn't work

        timestamp = dt_utc.isoformat() + "Z"


            # converting to CEST
        # dt_cest = dt_utc + timedelta(hours=2)     not needed - time converted in browser
        # timestamp = dt_cest.isoformat() + "Z"


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
                # 'id': 3,  
                'timestamp': timestamp,
                'latitude': latitude,
                'longitude': longitude,
                'speedKnots': speed_knots,
            }


    except Exception as e:
        print('Error while parsing', e)
        return None
        

    # testString = "$GPRMC,121525.000,A,5537.8451,N,01204.6738,E,0.16,317.18,050525,,,A*63"

    # messageParsed = (parse_gprmc(messageDecoded))

    # serialized = json.dumps(messageParsed)

    # headersArray = {'Content-type': 'application/json'}

    # response = requests.post("URL til vores REST service her", data = serialized, headers = headersArray)


while True: 
    message, clientAddress = serverSocket.recvfrom(2048)
    print("Received message:" + message.decode())
    messageDecoded = message.decode()
    modfiedMessage = messageDecoded.upper()
    parsed_data = parse_gprmc(messageDecoded)


    if parsed_data:
        try: 
                print(">> Parsed payload:", parsed_data)

                response = requests.post("https://restredning20250504122455.azurewebsites.net/api/GPSNew", json=parsed_data, timeout=5)
            
                print(f"Sent to REST API. Status: {response.status_code}")
        except requests.RequestException as e:
                print(f"Failed to send data to REST API: {e}")
        except Exception as e:
                print(f"Failed to send data to REST API: {e}")

    
  
    
    # print("Received message:" + message.decode())            



    

    


