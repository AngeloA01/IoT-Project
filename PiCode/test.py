import time
import smbus2


#Danger at various temps and humidities:

#high temp + high humidity causes risk of heatstroke
#low temp low humidity also dangerous

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

def movingAverage():
    if (lastTemps == [None] * 60):
        return False
    else:
        measured = 0
        runningSum = 0
        for x in range(0,60):
            if (lastTemps[x] != [None]):
                runningSum += lastTemps[x]
                measured += 1
            elif lastTemps[x] == [None]:
                average = runningSum/measured
                return average
        
def humidMovingAverage():
    if (lastHumid == [None] * 60):
        return False
    else:
        measured = 0
        runningSum = 0
        for x in range(0,60):
            if (lastHumid[x] != [None]):
                runningSum += lastHumid[x]
                measured += 1
            elif lastHumid[x] == [None]:
                average = runningSum/measured
                return average
        


counter = 0

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

        bus.i2c_rdwr(cmd_meas_humi)
        time.sleep(0.1)
        bus.i2c_rdwr(read_result)

        #convert the result to an int
        humidity = int.from_bytes(read_result.buf[0]+read_result.buf[1],'big')
        rel_humidity = ((125 * humidity)/65536) - 6
        print("Humidity: ", rel_humidity)

        time.sleep(2)

        lastTemps[counter%60] = celcius
        lastHumid[counter%60] = rel_humidity
        counter += 1
        print(movingAverage)

        

        # if counter == 10:
        #     #send data - Insert function here

except KeyboardInterrupt:
    active = False
 