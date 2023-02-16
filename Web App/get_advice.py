import read_all_data
# curr_CO2 = read_C02.get_C02()
# curr_pressure = read_pressure.get_pressure()
# curr_temp = read_temp_data.get_temperature()
# curr_tvoc = read_TVOC.get_TVOC()
curr_humidity = read_all_data.get_humidity()
curr_temp = read_all_data.get_temperature()
curr_tvoc = read_all_data.get_TVOC()
curr_pressure = read_all_data.get_pressure()
curr_CO2 = read_all_data.get_C02()
def getadvice():
    advices = ["It's hot outside, please drink lots of water", "Try drinking water"]
    if curr_temp>10:
        return advices[0]
    else:
        return advices[1]
print(getadvice())