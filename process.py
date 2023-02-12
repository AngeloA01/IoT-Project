import numpy
import math
import time
import dataclasses
import random
import matplotlib.pyplot as plt


timeScale = 10000 #1000 iterations

lastTemps = [None] * 60 #empty array

allTemps = [None] * timeScale

averageTempArray = [None] * timeScale

totalAverage = 0

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
        return runningSum/60


def addNewValue(iter, newVal):
        lastTemps[iter%60] = newVal


averageLine = [None] * timeScale
#Code Space
for a in range(0, timeScale):
    newtemp = (random.random()-0.5) + 20-(a/100000)
    addNewValue(a, newtemp) #20 +- 2.5 deg

    averageTempArray[a] = movingAverage()

    totalAverage = (totalAverage*(a) + newtemp)/(a+1)
    averageLine[a] = totalAverage


print(totalAverage)



plt.ylim([19, 21])

x1 = range (0, 60)
x2 = range(0, timeScale)
plt.title("All Temps")
#plt.plot (x2, allTemps, linewidth = '0.1')
plt.plot(x2, averageLine, linewidth = '2')
#plt.title("Moving Average")
plt.plot(x2, averageTempArray, linewidth = '1')
plt.show()













