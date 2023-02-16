import read_humidity1
# curr_CO2 = read_C02.get_C02()
# curr_pressure = read_pressure.get_pressure()
# curr_temp = read_temp_data.get_temperature()
# curr_tvoc = read_TVOC.get_TVOC()
curr_humidity = read_humidity1.get_humidity()
def getadvice():
    advices = ["It's hot outside, please drink lots of water", "Try drinking water"]
    if curr_humidity>10:
        return advices[0]
    else:
        return advices[1]
print(getadvice())