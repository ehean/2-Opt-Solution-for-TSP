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
    
    return math.sqrt(x_distance * x_distance + y_distance * y_distance)
    

    
def calculateTotalDistance(route):

    tot = 0.0
    for idx in range(0, len(route)-1):
        tot += calculateDistance(route[idx], route[idx+1])
    tot += calculateDistance(route[len(route)-1], route[0])
    
    return tot
        



 # 2optSwap(route, i, k) {
           # 1. take route[0] to route[i-1] and add them in order to new_route
           # 2. take route[i] to route[k] and add them in reverse order to new_route
           # 3. take route[k+1] to end and add them in order to new_route
           # return new_route;
       # }

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

 # repeat until no improvement is made {
           # start_again:
           # best_distance = calculateTotalDistance(existing_route)
           # for (i = 1; i < number of nodes eligible to be swapped - 1; i++) {
               # for (k = i + 1; k < number of nodes eligible to be swapped; k++) {
                   # new_route = 2optSwap(existing_route, i, k)
                   # new_distance = calculateTotalDistance(new_route)
                   # if (new_distance < best_distance) {
                       # existing_route = new_route
                       # goto start_again
                   # }
               # }
           # }
       # }
       

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


c1 = City(1, 0, 0)
c2 = City(2, 0, 1) 
c3 = City(3, 1, 1)
c4 = City(4, 1, 0)
c5 = City(5, .5, 2)
    

# construct an arbitrary solution
# this solution has one sub-optimal cross
# that needs to be fixed to get the optimal solution:
#   {c1, c2, c3, c4}
#   tot d = 4
fourCityProblem = []
fourCityProblem.append(c1)
fourCityProblem.append(c3)
fourCityProblem.append(c2)
fourCityProblem.append(c4)
    
print("INITIAL SET") 
sys.stdout.write("ORDER: ")
for c in fourCityProblem:
    sys.stdout.write(str(c.id) + ' ')
sys.stdout.write('\n')
    
print(calculateTotalDistance(fourCityProblem))
sys.stdout.write('\n')

s = findTSPSolution(fourCityProblem)

print("SOLUTION")  
sys.stdout.write("ORDER: ")
for c in s:
    sys.stdout.write(str(c.id) + ' ')
sys.stdout.write('\n')
    
print(calculateTotalDistance(s))
sys.stdout.write('\n')


c1 = City(1, 0, 0)
c2 = City(2, 1, 0) 
c3 = City(3, 1, 1)
c4 = City(4, .5, 2)
c5 = City(5, 0, 1)


# construct an arbitrary solution
# this solution has one sub-optimal cross
# that needs to be fixed to get the optimal solution:
#   {c1, c2, c3, c4}
#   tot d = 4
fiveCityProblem = []
fiveCityProblem.append(c1)
fiveCityProblem.append(c5)
fiveCityProblem.append(c2)
fiveCityProblem.append(c4)
fiveCityProblem.append(c3)

print("INITIAL SET")  
sys.stdout.write("ORDER: ")
for c in fiveCityProblem:
    sys.stdout.write(str(c.id) + ' ')
sys.stdout.write('\n')
    
print(calculateTotalDistance(fiveCityProblem))
sys.stdout.write('\n')

s = findTSPSolution(fiveCityProblem)

print("SOLUTION")  
sys.stdout.write("ORDER: ")
for c in s:
    sys.stdout.write(str(c.id) + ' ')
sys.stdout.write('\n')
    
print(calculateTotalDistance(s))
            
    