import time
import smbus2
import random
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

db = "https://embedded-lab-2-part-2-default-rtdb.europe-west1.firebasedatabase.app/"

# Define the private key file (change to use your private key)
keyfile = "/home/pi/privkey.json"

# Define the required scopes
scopes = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/firebase.database"
]

si7021_ADD = 0x40
si7021_READ_TEMPERATURE = 0xF3
si7021_READ_HUMIDITY = 0xF5
#no hold master mode

bus = smbus2.SMBus(1)
 #Set up a write transaction that sends the command to measure temperature
cmd_meas_temp = smbus2.i2c_msg.write(si7021_ADD,[si7021_READ_TEMPERATURE])

cmd_meas_humi = smbus2.i2c_msg.write(si7021_ADD,[si7021_READ_HUMIDITY])

#Set up a read transaction that reads two bytes of data
read_result = smbus2.i2c_msg.read(si7021_ADD,2)

active = True

# Authenticate a credential with the service account (change to use your private key)
credentials = service_account.Credentials.from_service_account_file(keyfile, scopes=scopes)

# Use the credentials object to authenticate a Requests session.
authed_session = AuthorizedSession(credentials)


try: 
    while (active):
        #Execute the two transactions with a small delay between them
        bus.i2c_rdwr(cmd_meas_temp)
        time.sleep(0.1)
        bus.i2c_rdwr(read_result)

        #convert the result to an int       
        temperature = int.from_bytes(read_result.buf[0]+read_result.buf[1],'big')
        celcius = ((175.72 * temperature)/65536) - 46.85
        print("Temperature: ", celcius)
        path = "temp_&_humidity.json"


        bus.i2c_rdwr(cmd_meas_humi)
        time.sleep(0.1)
        bus.i2c_rdwr(read_result)

        #convert the result to an int
        humidity = int.from_bytes(read_result.buf[0]+read_result.buf[1],'big')
        rel_humidity = ((125 * humidity)/65536) - 6
        print("Humidity: ", rel_humidity)
        
        data = {"Temperature: ": celcius, "Humidity: ": rel_humidity}
        response = authed_session.post(db+path, json=data)

        if response.ok:
            print("Created new node named {}".format(response.json()["name"]))
        else:
            raise ConnectionError("Could not write to database: {}".format(response.text))

        time.sleep(1.8)

except KeyboardInterrupt:
    active = False