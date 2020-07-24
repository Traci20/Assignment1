'''
Name : Traci Ewurabena Nhyira Gyebi
ID : 37242022
Assignment 2
'''

'''
Brief Introduction of the code - It generates random numbers between 1 and 32767
and performs both a binary search and interpolation search. Then compares the time it
takes to perform both searches.

This particular code only contains the Interpolation search function
'''

# Time and random are packages imported to help run the code
# Time - helps in the calculation of time
# Random - Helps in generating random numbers

import time
import random

# If items is present in alist[0..n-1], then returns 
# index of it, else returns false 
def InterpolationSearch(alist, n, items): 
# Finding the index of both low and high positions
    low = 0
    high = (n - 1) 
   
# Because the array is sorted, an element present in array must be in range defined by corner  
    while low <= high and items >= alist[low] and items <= alist[high]: 
        if low == high: 
            if alist[low] == items:  
                return low; 
            return False; 
          
# Probing the position with keeping uniform distribution in mind.  
        pos  = low + int(((float(high - low) / 
            ( alist[high] - alist[low])) * ( items - alist[low]))) 
  
# Condition for finding target 
        if alist[pos] == items: 
            return True 
   
# If items is larger, items is in the higher position
        if alist[pos] < items: 
            low = pos + 1; 
   
# If items is smaller, items is in the lower position 
        else: 
            high = pos - 1; 
      
    return False

'''
This code(function) is an Interpolation Search which is an improvement over Binary Search for instances,
where the values in a sorted array are uniformly distributed.
Unlike Binary search which searches from the midpoint, interpolation search may go to different locations according
to the value of the key being searched. For example, if the value of the key is
closer to the last element, interpolation search is likely to start search toward the end side.
'''




