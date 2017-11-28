"""
Program:    2-Opt Approximation of TSP 
Name:       Erik Heaney
            Matthew Scott
            Kyle De Laurell
Date:       11/26/2017
Course:     CS 325 Fall 2017
Description:
This is the final project for CS 325. It is the
implementation of the 2-Opt algorithm, which finds
an approximate solution to the TSP. 

Below is psuedocode, from https://en.wikipedia.org/wiki/2-opt:

    2optSwap(route, i, k) {
           1. take route[0] to route[i-1] and add them in order to new_route
           2. take route[i] to route[k] and add them in reverse order to new_route
           3. take route[k+1] to end and add them in order to new_route
           return new_route;
       }
   
    repeat until no improvement is made {
           start_again:
           best_distance = calculateTotalDistance(existing_route)
           for (i = 1; i < number of nodes eligible to be swapped - 1; i++) {
               for (k = i + 1; k < number of nodes eligible to be swapped; k++) {
                   new_route = 2optSwap(existing_route, i, k)
                   new_distance = calculateTotalDistance(new_route)
                   if (new_distance < best_distance) {
                       existing_route = new_route
                       goto start_again
                   }
               }
           }
       }
"""
import math
import sys

class City  :
    
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        
        
        
def calculateDistance(city1, city2):

    x_distance = abs(city1.x - city2.x)
    y_distance = abs(city1.y - city2.y)
    
    return int(round(math.sqrt(x_distance * x_distance + y_distance * y_distance)))
   
def fileImport(filename):
    with open (filename, "r") as myfile:
        #initializes variables
        counter = 0
        setCounter = 0

        #loops through each line of file to gather data
        Cities = []
        for line in myfile:
            numArray = []
            lineNumbers = line.split()
            for num in lineNumbers:
                numArray.append(int(num))
            Cities.append(City(numArray[0], numArray[1], numArray[2]))

    return Cities

# Writes output to file named after the original import file with .tour appended
def fileExport(fileName, tour, distance):
    with open (fileName + ".tour", "w") as myFile:
        myFile.write(str(distance) + '\n')
        for city in tour:
            myFile.write("%d\n" % city.id)

    
def calculateTotalDistance(route):

    tot = 0
    for idx in range(0, len(route)-1):
        tot += calculateDistance(route[idx], route[idx+1])
    tot += calculateDistance(route[len(route)-1], route[0])
    
    return tot
        

def twoOptSwap(route, i, k):
    new_route = []
    
    # 1. take route[0] to route[i-1] and add them in order to new_route
    for index in range(0, i):
        new_route.append(route[index])
    
    # 2. take route[i] to route[k] and add them in reverse order to new_route
    for index in range(k, i-1, -1):
        new_route.append(route[index])
    
    # 3. take route[k+1] to end and add them in order to new_route
    for index in range(k+1, len(route)):
        new_route.append(route[index])
    
    return new_route

def findTSPSolution(s):       
    improvement = True

    while improvement: 
        improvement = False
        best_distance = calculateTotalDistance(s)
        i = 1
        while i < len(s):
            for k in range(i+1, len(s)):
                new_route = twoOptSwap(s, i, k)
                new_distance = calculateTotalDistance(new_route)
                if new_distance < best_distance:
                    s = new_route[:]
                    best_distance = new_distance
                    improvement = True
                    i = 1
            else:
                i += 1   

    return s  

def printTour(s):
    sys.stdout.write("ORDER: ")
    for c in s:
        sys.stdout.write(str(c.id) + ' ')
    print("\nDistance: " + str(calculateTotalDistance(s)))


if len(sys.argv) < 2:
	print("Please enter the file name")
	exit()

s = fileImport(sys.argv[1])

print("\nINITIAL SOLUTION")  
printTour(s)

s = findTSPSolution(s)
fileExport(sys.argv[1], s, calculateTotalDistance(s))

print("\n2OPT SOLUTION")  
printTour(s)
