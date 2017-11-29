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
an approximate solution to the TSP. It does by first:
    1. Constructing a decent solution
    2. Improving that solution by making the locally
       optimal choices.
 
Below is the nearest neighbor psuedocode, used for the 
construction heuristic, from https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm:

    1. start on an arbitrary vertex as current vertex.
    2. find out the shortest edge connecting current vertex and an unvisited vertex V.
    3. set current vertex to V.
    4. mark V as visited.
    5. if all the vertices in domain are visited, then terminate.
    6. Go to step 2.

Below is the 2-Opt psuedocode, from https://en.wikipedia.org/wiki/2-opt:

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
import time

class City  :
    
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.visited = False
          
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
def fileExport(filename, tour, distance):
    with open (filename + ".tour", "w") as myFile:
        myFile.write(str(distance) + '\n')
        for city in tour:
            myFile.write("%d\n" % city.id)

    
def calculateTotalDistance(route):

    tot = 0
    for idx in range(0, len(route)-1):
        tot += calculateDistance(route[idx], route[idx+1])
    tot += calculateDistance(route[len(route)-1], route[0])
    
    return tot
        
        
# 1. start on an arbitrary vertex as current vertex.
# 2. find out the shortest edge connecting current vertex and an unvisited vertex V.
# 3. set current vertex to V.
# 4. mark V as visited.
# 5. if all the vertices in domain are visited, then terminate.
# 6. Go to step 2
        
        
def findClosestNeighbor(v, route):
    
    shortestEdgeLength = 99999999999
    closestNeighbor = None
    for c in route:
        if c.id != v.id:
            distance = calculateDistance(v, c)
            if shortestEdgeLength > distance:
                closestNeighbor = c
                shortestEdgeLength = distance
                
    return closestNeighbor
    
# @profile
def nearestNeighbor(route):
    new_route = []
    current_city = route.pop(0)
    new_route.append(current_city)
    while route != []:
        next = findClosestNeighbor(current_city, route)
        current_city = next
        route.remove(next)
        new_route.append(current_city)
        
    return new_route
        
    
    
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

# @profile
def findTSPSolution(s, timeAvailable):       
    improvement = True
    start = time.time()
    end = start + timeAvailable
    while improvement: 
        improvement = False
        best_distance = calculateTotalDistance(s)
        i = 1
        while i < len(s):
            for k in range(i+1, len(s)):
                new_route = twoOptSwap(s, i, k)
                new_distance = calculateTotalDistance(new_route)
                if new_distance < best_distance:
                    s = new_route
                    best_distance = new_distance
                    improvement = True
                    i = 1
                if time.time() > end:
                    return s
            else:
                i += 1   

    return s  

def printTour(s):
    # sys.stdout.write("ORDER: ")
    # for c in s:
    #     sys.stdout.write(str(c.id) + ' ')
    print("Distance: " + str(calculateTotalDistance(s)))

 
start = time.time()
totalTime = 179.0
if len(sys.argv) < 2:
	print("Please enter the file name")
	exit()

filename = sys.argv[1]
s = fileImport(filename)

print("\nINITIAL SOLUTION")  
printTour(s)

greedy = nearestNeighbor(s)
s = fileImport(filename)

print("\nAFTER NEAREST NEIGHBOR PASS")  
printTour(greedy)

if calculateTotalDistance(greedy) < calculateTotalDistance(s):
    s = greedy
else:
    print("Greedy solution discarded.")

timeAvailable = totalTime - (time.time() - start)
s = findTSPSolution(s, timeAvailable)
fileExport(filename, s, calculateTotalDistance(s))

print("\nAFTER 2OPT")  
printTour(s)
end = time.time()
timeElapsed = end - start
print("TIME: %f" % timeElapsed)