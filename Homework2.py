'''
Name - Traci Ewurabena Nhyira Gyebi
ID - 37242022

This function calculates the dot product of a list of values
with the same size but have been randomized to generate the
values.

'''
import random # This imports the entire package of random


def DotProduct(N, ListA, ListB):
    dotproduct = [i*j for i, j in zip(ListA, ListB)]
    dprod = sum(dotproduct)
    print ("The dot product of ListA and ListB is" + " " + str(dprod))
    
'''
zip returns an iterator of the tuples where i-th tuple
contains the i-th element from each of the argument sequence
and j-th tuple contains the j-th element from each of the argument tuple.
It stops when the shortest input iterable is exhausted.
''' 
'''
After the zip module multiplies the various indexes of
the two lists, dprod sums the new list of the values
together to produce the actual dot product which is a scalar.
'''    
    
    
    

        
    
    
 
 
   