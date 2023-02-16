import read_all_data
import random
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
#     advices = ["It's hot outside, please drink lots of water", "Try drinking water"]
#     if curr_temp>10:
#         return advices[0]
#     else:
#         return advices[1]
        return ProcessTuple()
#end of ziyad's test code

#start of angelos code, you can change this however and then just print to make sure it only prints out one advice statement
#then run the server.py file and go to http://127.0.0.1:8000 (cmd/ctrl click on that link) and
#it'll show the checkmyhealth.html file and click the button and check that the advice it shows is correct

messageTuple = [False, False, False, False, False, False]
#High heat, high humidity, cold, ice warning, high CO2, high TVoC

def tupleAssignment():
        if (curr_temp > 20) :
                messageTuple[0] = True

        if (curr_humidity > 50):
                messageTuple[1] = True

        if (curr_temp < 0): messageTuple[3] = False

        elif (curr_temp < 10):
                messageTuple[2] = True

        if (curr_CO2 > 500):
                messageTuple[4] = True

        if (curr_tvoc > 1000):
                messageTuple[5] = True


def ProcessTuple():
        messages = ["Hot weather alert, stay hydrated and use suncream. ", #0
                        "Dry conditions warning, ensure you drink enough water and stay in the shade", #1
                        "Hot, humid conditions, try to stay in the shade", #2
                        "Cold conditions, wear warm clothes",  #3
                        "Sub-zero temperatures, wear warm clothes and be wary of ice.", #4
                        "Conditions nominal, no precautions necessary", #5
                        "Lots of CO2, wear a mask", #6
                        "High air pollution, ventilate the room or wear a mask"]#7

        outmessage = []

        if messageTuple == [False]*6:
                return messages[5]     #default message
        else:
                if messageTuple[0] and not messageTuple[1]: 
                        outmessage.append(messages[0])
                        outmessage.append(messages[2])

                if messageTuple[0] and messageTuple[1]: 
                        outmessage.append(messages[1])

                if messageTuple[3]: 
                        outmessage.append(messages[3])

                if messageTuple[3] and messageTuple[4]:
                        outmessage.append(messages[4])

                if messageTuple[4]:
                        outmessage.append(messages[6])

                if len(outmessage) > 1:
                        rand = random.randint(0, len(outmessage)-1)
                        return outmessage[rand]
        


                


tupleAssignment()
print(ProcessTuple())

