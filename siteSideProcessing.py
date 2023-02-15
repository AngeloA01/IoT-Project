import time
from datetime import datetime
import random
import matplotlib.pyplot as plt
import math

#import the JSONs here: 
#process JSON: get out the values and put them into arrays

#returns a temp with gauss noise 
def randTemp(min):
    return 25 + random.gauss(0, 0.5)

#Processing options: 
#total average temperature for the whole day: 

arrayConst = 144 #144 points for the day, a time every 10 mins
timePeriod = 10

tempArray = [None] * arrayConst

def getAvg(arr):
    length = arr.len()
    avg = sum(arr)/length
    return avg

def getMinute():
    now = datetime.now()
    return now.hour * 60 + now.minute

def plotTemps():
    plt.xlabel("Times")
    plt.ylabel("Temp, C")
    plt.plot(range(0, 144), tempArray)
    plt.axis([0, 144, 0, 40])
    plt.show()

def dateParser(d):
    #returns minute
    return d.hour * 60 + d.minute

def addtoArrays(temp, dateData):
    #min = getMinute()
    min = dateParser(dateData)
    index = int(min/10)
    if tempArray[index] == None:
        tempArray[index] = temp
        

    

    

# def allFunc():
#     #the goal of this function is to plot a series of values 
#     #All of these should ideally be on the same graph
#     #For demonstration, matplotlib is used here (python3.9 needed to run)
#     #Assumption: For a single day, we use an array of length 6-12*24 = 144 - 288
#     #minute_of_day = getMinute()

    
    




#Main section: 
Temp = 25 #Degrees Celcius
Humid = 45 # rel
Pressure = 1020 #HPa
Co2 = 400 #PPM
TVoC = 0.1 #PPB
Date = datetime.now() #Only need day, hour, minute. 
exampleJSON = {Temp, Humid, Pressure, Co2, TVoC, Date}

addtoArrays(Temp, Date)

for x in range(arrayConst):
    if (tempArray[x] != None):
        print(tempArray[x], x)



