'''
Name : Traci Ewurabena Nhyira Gyebi
ID : 37242022
Assignment 2
'''

'''
Brief Introduction of the code - It generates random numbers between 1 and 32767
and performs both a binary search and interpolation search. Then compares the time it
takes to perform both searches.

This particular code only contains the Binary search function
'''

# Time and random are packages imported to help run the code
# Time - helps in the calculation of time
# Random - Helps in generating random numbers

import time
import random

def binarySearch(alist, item):
# Finding the index of both low and high positions
    low = 0
    high = len(alist)-1
    found = False
    
# Because the array is sorted, an element present in array must be in range defined by corner 
    while low <= high and not found:
        midpoint = (low + high)//2
        
# Condition for finding target
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                high = midpoint - 1
            else: low = midpoint+1
    return found

'''
This code(function) is a binary search which is an efficient algorithm for finding
an item from a sorted list of items. It works by repeatedly
dividing in half the portion of the list that could contain
the item, until you've narrowed down the possible locations to just one.
'''