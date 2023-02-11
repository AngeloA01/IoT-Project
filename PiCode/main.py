import time
import smbus2
import board
import adafruit_bmp280
# Sets up I2C for atomospheric pressure
import random
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
√
i2cbmp = board.I2C()
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2cbmp)

#data base code________________---------------_____________----------______________-------------__________

db = "https://embedded-lab-2-part-2-default-rtdb.europe-west1.firebasedatabase.app/"

# Define the private key file (change to use your private key)
keyfile = "/home/pi/privkey.json"

# Define the required scopes
scopes = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/firebase.database"
]

# Authenticate a credential with the service account (change to use your private key)
credentials = service_account.Credentials.from_service_account_file(keyfile, scopes=scopes)

# Use the credentials object to authenticate a Requests session.
authed_session = AuthorizedSession(credentials)

#data base code________________---------------_____________----------______________-------------__________

si7021_ADD = 0x40
si7021_READ_TEMPERATURE = 0xE3
si7021_READ_HUMIDITY = 0xE5

bus = smbus2.SMBus(1)

#Set up a write transaction that sends the command to measure temperature
cmd_meas_temp = smbus2.i2c_msg.write(si7021_ADD,[si7021_READ_TEMPERATURE])
cmd_meas_hum = smbus2.i2c_msg.write(si7021_ADD,[si7021_READ_HUMIDITY])
#Set up a read transaction that reads two bytes of data
read_result = smbus2.i2c_msg.read(si7021_ADD,2)


while(1):
    # reads atmospheric pressure data
    try:
        print('Temperature: {} degrees C'.format(sensor.temperature))
        print('Pressure: {}hPa'.format(sensor.pressure))
        pressure = sensor.pressure
        
        path = "pressure.json"

        data = {"pressure: ": pressure}
        response = authed_session.post(db+path, json=data)
    # prints error
    except:
        print('bmp error')
    time.sleep(0.5)

    #Execute the two transactions with a small delay between them
    bus.i2c_rdwr(cmd_meas_temp)
    time.sleep(0.1)

    bus.i2c_rdwr(read_result)

    #convert the result to an int
    temperature = int.from_bytes(read_result.buf[0]+read_result.buf[1],'big')
    celcius = ((175.72 * temperature)/65536) - 46.85
    print("temperature", celcius)
    time.sleep(0.5)
    
    path1 = "temperature.json"

    data = {"temperature: ": celcius}
    response = authed_session.post(db+path1, json=data)

    bus.i2c_rdwr(cmd_meas_hum)
    time.sleep(0.1)
    bus.i2c_rdwr(read_result)


    humidity = int.from_bytes(read_result.buf[0]+read_result.buf[1],'big')
    percent_hum = ((125*humidity)/65536)-6
    
    path2 = "humidity.json"

    data = {"Humidity: ": percent_hum}
    response = authed_session.post(db+path2, json=data)

    if response.ok:
        print("Created new node named {}".format(response.json()["name"]))
    else:
       raise ConnectionError("Could not write to database: {}".format(response.text))


    print("relative humidity:", percent_hum)
    time.sleep(2)
