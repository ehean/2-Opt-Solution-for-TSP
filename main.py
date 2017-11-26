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