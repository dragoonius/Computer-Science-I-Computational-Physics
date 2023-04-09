# -*- coding: utf-8 -*-
import random
import numpy
import matplotlib.pyplot as plt
"""
Created on Thu Oct 13 17:12:56 2022

@author: Joseph Helsing
"""

def main():
    
    synthData = [-1,391,408,403,389,-1,439,397,429,410,-1,-1,-1,435,-1,351,415,401,415,-1]
    interpolatedData = []
    
    print("Welcome to the sensor simulator!")
    
    choice = 0
    while choice != 7:
        choice = menu()  

        if choice == 1:
            synthData = generateDataset()
        elif choice == 2:
            interpolatedData = interpolateMinutes(1,synthData)
        elif choice == 3:
            interpolatedData = interpolateMinutes(2,synthData)
        elif choice == 4:
            interpolatedData = interpolateMinutes(3,synthData)
        elif choice == 5:
            interpolatedData = interpolateGlobal(synthData)
        elif choice == 6:
            compareData(synthData,interpolatedData)
        elif choice == 7:
            print("Thank you for using the simulator!")   
        else:
            print(f"{choice} is not a valid choice")   

def menu(): 
    print("")
    print("Menu:")
    print("1. Generate a synthetic dataset")
    print("2. Interpolate with 2 minutes")
    print("3. Interpolate with 4 minutes")
    print("4. Interpolate with 6 minutes")
    print("5. Interpolate with all minutes")
    print("6. Output data comparison")
    print("7. Exit")
    
    choice = int(input("Please enter a choice: "))
    print("")
    
    return choice



def outputValues(prefix,data):
    print(prefix,end="") 
    for x in data:
        print("%4d" % (x),end="")        
    print("")
    
def generateDataset():
    """Takes in two numbers, returns their sum."""
    
    time = int(input("How many minutes would you like to generate data for (10 or more minutes): "))
    
    while(time < 10):
        print(f"{time} minutes is too brief! Please enter a time that is 10 minutes or more.")
        time = int(input("How many minutes would you like to generate data for (10 or more minutes): "))
        
    
    tempList = []
    
    for x in range(time):
        if random.randint(1, 5) == 5:
            tempList.append(-1)
        else:
            tempList.append(random.randint(350, 450))
    
    
    outputValues("Min:  ",range(time))
    outputValues("Temp: ",tempList)
    
    return tempList

 
def calcMean(calList):
    total = 0
    count = 0
    
    for x in calList:
        if x != -1:
            total += x
            count += 1
            
    if count == 0:
        return -1
            
    return total/count

def calcVariance(calList,avg):
    total = 0
    count = 0
    
    for x in calList:
        if x != -1:
            total += (x - avg)**2
            count += 1

    return total/(count-1)
       
def interpolateMinutes(minutes,synthData):
    print(f"Interpolating with {minutes*2} minutes")
    tempList = []
    
    for x in range(len(synthData)):
        if synthData[x] != -1:
            tempList.append(synthData[x])
        elif x == 0:
            tempRight = synthData[1:1+minutes]
            avg = calcMean(tempRight)
            tempList.append(avg)
        elif x == len(synthData) - 1:
            tempLeft = synthData[len(synthData)-1-minutes:]
            avg = calcMean(tempLeft)
            tempList.append(avg)
        else:
            tempRight = synthData[x+1:x+1+minutes]
            tempLeft = synthData[x-minutes:x]
            tempFull = tempRight + tempLeft
            avg = calcMean(tempFull)
            tempList.append(avg)
            
    return tempList
            

def interpolateGlobal(synthData):
    print("Interpolating with all minutes")
    tempList = []
    average = calcMean(synthData)
    
    for x in range(len(synthData)):
        if synthData[x] != -1:
            tempList.append(synthData[x])
        else:
            tempList.append(average)
            
    return tempList
    
def compareData(synthData,interpolatedData):
    
   if  len(interpolatedData) == 0:
       print("Please use one of the interpolation strategies before outputting data!")
       return
    
   origMean = 0
   origVariance = 0
   origStdDev = 0
   interMean = 0
   interVariance = 0
   interStdDev = 0
    
   outputValues("Min:  ",range(len(synthData)))
   outputValues("Temp: ",synthData)
   outputValues("Temp: ",interpolatedData)
    
   origMean = calcMean(synthData)   
   origVariance = calcVariance(synthData, origMean)
   origStdDev = numpy.sqrt(origVariance)
   
   print("\nOriginal Data Set")
   print("Mean: %.2f" % origMean)
   print("Variance: %.2f" % origVariance)
   print("Standard Deviation: %.2f" % origStdDev)
   
   interMean = calcMean(interpolatedData)
   interVariance = calcVariance(interpolatedData, interMean)
   interStdDev = numpy.sqrt(interVariance)
   
   print("\nInterpolated Data Set")
   print("Mean: %.2f" % interMean)
   print("Variance: %.2f" % interVariance)
   print("Standard Deviation: %.2f" % interStdDev)
   
   plt.plot(range(0,len(synthData)), synthData, color='red', marker='o')
   plt.plot(range(0,len(interpolatedData)), interpolatedData, color='blue', marker='o')
   plt.title('Synthetic Data vs Interpolated Data', fontsize=14)
   plt.xlabel('Minutes', fontsize=14)
   plt.ylabel('Temperature', fontsize=14)
   plt.grid(True)
   plt.show()
      
    
main()
