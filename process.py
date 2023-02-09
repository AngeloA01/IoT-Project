import numpy
import math
import time
import dataclasses
import random
import matplotlib.pyplot as plt





#Function Definitions
timeScale = 1000 #1000 iterations

lastTemps = [None] * 60 #empty array

allTemps = [None] * timeScale

averageTempArray = [None] * timeScale

# a = (0, 1, 1, 1, 2, 3, 7, 7, 23)

#  def count_elements(seq) -> dict:
#      """Tally elements from `seq`."""
#      hist = {}
#    for i in seq:
# hist[i] = hist.get(i, 0) + 1
# return hist

# >>> counted = count_elements(a)
# >>> counted
# {0: 1, 1: 3, 2: 1, 3: 1, 7: 2, 23: 1}



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

#Code Space
for a in range(0, timeScale):

    addNewValue(a, (random.random()-0.5) + 20) #20 +- 2.5 deg

    averageTempArray[a] = movingAverage()



x1 = range (0, 60)
x2 = range(0, timeScale)
plt.title("All Temps")
plt.plot (x2, allTemps)
#plt.title("Moving Average")
plt.plot(x2, averageTempArray)
plt.show()













