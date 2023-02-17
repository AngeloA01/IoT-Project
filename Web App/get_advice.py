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
        # messages = ["Hot weather alert, stay hydrated and use suncream. ", #0
        #                 "Dry conditions warning, ensure you drink enough water and stay in the shade", #1
        #                 "Hot, humid conditions, try to stay in the shade", #2
        #                 "Cold conditions, wear warm clothes",  #3
        #                 "Sub-zero temperatures, wear warm clothes and be wary of ice.", #4
        #                 "Conditions nominal, no precautions necessary", #5
        #                 "Lots of CO2, wear a mask", #6
        #                 "High air pollution, ventilate the room or wear a mask", 
        #                 ""]#7

        CO2_messages = ["Lot's of CO2, wear a mask. ", "Traffic must be crazy, CO2 excess detected. ",
        "Lot of air pollution. ", "High CO2 Detected, act accordingly. "]
        TVoC_messages = ["Air pollution is quite high here. ", "Wear a mask, hazardous levels of particles detected. ",
        "Consider opening a window if indoors, high Pollution. ", "Ensure you are wearing a mask! Lots of pollution"]
        heat_messages = ["It's hot, drink some water. ", "High temperatures detected, make stay in the shade. ", "Very high temperatures detected. Stay cool", 
        "Wow, it is scorching! Stay safe and cool."]
        cold_messages = ["Quite Cold, wear something warm!", "Make sure to wear a coat. ", "It's quite cold! "]
        ice_messages = ["Sub zero temperatures, wear warm clothes and watch out for ice!", "It's really cold, wear warm clothes!", "Ice warning, watch out. ", 
        "You might be able to make a snowman, it's cold enough for snow!"]
        humidity_messages = ["You must be in a jungle, it's ridiculously humid. ", "Quite humid and hot, stay safe. ",
        "High humidity detected!"]
        pressure_messages = ["pressure nominal.  ", "pressure high. ", "pressure low"]


        outmessage = ""

        # if messageTuple == [False]*6:
        #         return messages[5]     #default message
        # else:
        #         if messageTuple[0] and not messageTuple[1]: 
        #                 outmessage.append(messages[0])
        #                 outmessage.append(messages[2])

        #         if messageTuple[0] and messageTuple[1]: 
        #                 outmessage.append(messages[1])

        #         if messageTuple[3]: 
        #                 outmessage.append(messages[3])

        #         if messageTuple[3] and messageTuple[4]:
        #                 outmessage.append(messages[4])

        #         if messageTuple[4]:
        #                 outmessage.append(messages[6])

        #         if len(outmessage) > 1:
        #                 rand = random.randint(0, len(outmessage)-1)
        #                 return outmessage[rand]
        if (350 <curr_CO2 < 450):
                outmessage += "Nominal CO2 Levels. "
        else: 
                if curr_CO2 > 450: 
                        rand = random.randint(0, len(CO2_messages)-1)
                        outmessage += CO2_messages[rand]

        if (10 < curr_temp < 20):
                outmessage += "Temperature Conditions Nominal. "
        else: 
                if curr_temp > 20: 
                        rand = random.randint(0, len(heat_messages)-1)
                        outmessage+= heat_messages[rand]
                if curr_temp < 0:
                        rand = random.randint(0, len(ice_messages)-1)
                        outmessage+= ice_messages[rand]
                elif curr_temp < 10:
                        rand = random.randint(0, len(cold_messages)-1)
                        outmessage+= cold_messages[rand]

        if (30 < curr_humidity < 60):
                outmessage += "Humidity is nominal. "
        else: 
                if (curr_humidity < 30):
                        if curr_temp > 25:
                                outmessage+= "Quite hot and dry, stay safe. "

                elif  (curr_humidity > 60):
                        if curr_temp > 25:
                                outmessage += humidity_messages[1]

                        else: 
                                rand = randint(0, 1)
                                if rand == 0:
                                        outmessage+= humidity_messages[0]
                                else: 
                                        outmessage+= humidity_messages[2]
        if (curr_tvoc < 50):
                outmessage += "Nominal TVoC Levels. "
        else: 
                if curr_tvoc > 50: 
                        rand = random.randint(0, len(TVoC_messages)-1)
                        outmessage+= TVoC_messages[rand]

        return outmessage
                        


                

                
        


                


tupleAssignment()
print(ProcessTuple())
