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
#end of ziyad's test code

#start of angelos code, you can change this however and then just print to make sure it only prints out one advice statement
#then run the server.py file and go to http://127.0.0.1:8000 (cmd/ctrl click on that link) and
#it'll show the checkmyhealth.html file and click the button and check that the advice it shows is correct
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
print(getadvice())