import time
import smbus2
import board
import adafruit_bmp280
# Sets up I2C for atomospheric pressure
i2cbmp = board.I2C()
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2cbmp)

si7021_ADD = 0x40
si7021_READ_TEMPERATURE = 0xE3
si7021_READ_HUMIDITY = 0xE5

bus = smbus2.SMBus(1)
start = 1

#Set up a write transaction that sends the command to measure temperature
cmd_meas_temp = smbus2.i2c_msg.write(si7021_ADD,[si7021_READ_TEMPERATURE])
cmd_meas_hum = smbus2.i2c_msg.write(si7021_ADD,[si7021_READ_HUMIDITY])
#Set up a read transaction that reads two bytes of data
read_result = smbus2.i2c_msg.read(si7021_ADD,2)


while(start == 1):
    # reads atmospheric pressure data
    try:
        print('Temperature: {} degrees C'.format(sensor.temperature))
        print('Pressure: {}hPa'.format(sensor.pressure))
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

    bus.i2c_rdwr(cmd_meas_hum)
    time.sleep(0.1)
    bus.i2c_rdwr(read_result)


    humidity = int.from_bytes(read_result.buf[0]+read_result.buf[1],'big')
    percent_hum = ((125*humidity)/65536)-6

    print("relative humidity:", percent_hum)
    time.sleep(0.5)
