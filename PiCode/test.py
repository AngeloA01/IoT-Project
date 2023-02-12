import time
import smbus2
import random
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
import board
import adafruit_bmp280
import RPi.GPIO as GPIO

#GPIO setup for button
# BUTTONPIN = 10

# GPIO.setwarnings(False) 
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(BUTTONPIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #pin 17



# Sets up I2C for atomospheric pressure
i2cbmp = board.I2C()
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2cbmp)


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

totalAverageTemp = 0
totalAverageHumid = 0

lastTemps = [None] * 60 #empty array
lastHumid = [None] * 60
lastPress = [None] * 60



def movingAverage():
    if (lastTemps == [None] * 60):
        return False
    else:
        measured = 0
        runningSum = 0
        for x in range(0,60):
            if (lastTemps[x] != None):
                runningSum += lastTemps[x]
                measured += 1
            elif lastTemps[x] == None:
                average = runningSum/measured
                return average
        
def humidMovingAverage():
    if (lastHumid == [None] * 60):
        return False
    else:
        measured = 0
        runningSum = 0
        for x in range(0,60):
            if (lastHumid[x] != None):
                runningSum += lastHumid[x]
                measured += 1
            elif lastHumid[x] == None:
                average = runningSum/measured
                return average


def pressureMovingAverage():
    if (lastPress == [None] * 60):
        return False
    else:
        measured = 0
        runningSum = 0
        for x in range(0,60):
            if (lastPress[x] != None):
                runningSum += lastPress[x]
                measured += 1
            elif lastPress[x] == None:
                average = runningSum/measured
                return average
        


#tuple definitions: moderate heat warning, dry conditions, moderate cold warning, ice warning
messageTuple = {False, False, False, False}

def tupleUpdate():
    if movingAverage() > 25 and humidMovingAverage() > 40:
        messageTuple[0] = True
    else: messageTuple[0] = False

    if humidMovingAverage() < 40 and movingAverage() > 30:
        messageTuple[0] = True
        messageTuple[1] = True
    else: 
        messageTuple[0] = False
        messageTuple[1] = False

    if movingAverage() < 10:
        messageTuple[3] = True

    else: messageTuple[3] = False

    if movingAverage < 1: 
        messageTuple[4] = True

    else: False




def sendMessage(msg):
    global messageSend
    messageSend = msg

def ProcessTuple():
    messages = {"Hot weather alert, stay hydrated and use suncream. ", 
                "Dry conditions warning, ensure you drink enough water and stay in the shade", 
                "Hot, humid conditions, try to stay in the shade", 
                "Cold conditions, wear warm clothes", 
                "Sub-zero temperatures, wear warm clothes and be wary of ice.",
                "Conditions nominal, no precautions necessary"}

    if messageTuple == {False, False, False, False}:
        sendMessage(messages[5])
        #default message
    else:
        if messageTuple[0] and not messageTuple[1]: 
            sendMessage(messages[0])
            sendMessage(messages[2])

        if messageTuple[0] and messageTuple[1]: 
            sendMessage(messages[1])

        if messageTuple[3]: 
            sendMessage(messages[3])

        if messageTuple[3] and messageTuple[4]:
            sendMessage[messages[4]]


counter = 0
try: 
    while (active):


       # print("Pressure, hPa= ", sensor.pressure)

        #Execute the two transactions with a small delay between them
        bus.i2c_rdwr(cmd_meas_temp)
        time.sleep(0.1)
        bus.i2c_rdwr(read_result)

        #convert the result to an int
        temperature = int.from_bytes(read_result.buf[0]+read_result.buf[1],'big')
        celcius = ((175.72 * temperature)/65536) - 46.85
        #print("Temperature, C: ", celcius)

        bus.i2c_rdwr(cmd_meas_humi)
        time.sleep(0.1)
        bus.i2c_rdwr(read_result)

        #convert the result to an int
        humidity = int.from_bytes(read_result.buf[0]+read_result.buf[1],'big')
        rel_humidity = ((125 * humidity)/65536) - 6
       # print("Humidity, relative: ", rel_humidity)

      
        time.sleep(2)

        lastTemps[counter%60] = celcius
        lastHumid[counter%60] = rel_humidity
        lastPress[counter%60] = sensor.pressure
        counter += 1
        print("Temperature Moving Average: ", movingAverage())
        print("Humidity Moving Average   : ", humidMovingAverage())
        print("Pressure Moving Average   : ", pressureMovingAverage())

        totalAverageTemp = (totalAverageTemp*(counter) + celcius)/(counter+1)

        

        # path = "temp_&_humidity.json"
        # data = {"Temperature: ": celcius, "Humidity: ": rel_humidity}
        # response = authed_session.post(db+path, json=data)

        # if response.ok:
        #     print("Created new node named {}".format(response.json()["name"]))
        # else:
        #     raise ConnectionError("Could not write to database: {}".format(response.text))
        # # if counter == 10:
        # #     #send data - Insert function here
except KeyboardInterrupt:
    active = False
 