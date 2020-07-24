'''
Name : Traci Ewurabena Nhyira Gyebi
ID : 37242022
Assignment 2
'''
'''
This is the test file for the class deque
'''
from question1 import *

Meck = Deque()
print('The items in the array: ', Meck.display_items())
print('Is the array empty?', Meck.isEmpty())
print('Is the array full?', Meck.isFull())
print('What is the size of the array?', Meck.size())
#  This code initialises an instance of the deque to be half-full.
# And since the maxarraysize is 20, 10 will make it half full
N = 20
for i in range(N//2):
    bonus = random.randint(1,100)
    Meck.add_to_rear(bonus)
    
print(' ')
print('The simulations for the first row')
# items generates random numbers between 0 and 1 for the probability table
items = random.uniform(0,1)
print('Random number generated between 0 and 1:', items)

# the cummulative intervals for the probability table is as follows: 
if items > 0 and items <= 0.1:
    geeb = random.randint(1,100)
    print('The random number generated between 1 and 100:', geeb)
    Meck.add_to_front(geeb)

if items > 0.1 and items <= 0.3:
    geeb = random.randint(1,100)
    print('The random number generated between 1 and 100:', geeb)
    Meck.remove_from_front()
    
if items > 0.3 and items <= 0.4:
    geeb = random.randint(1,100)
    print('The random number generated between 1 and 100:', geeb)
    Meck.add_to_rear(geeb)
    
if items > 0.4 and items <= 1:
    geeb = random.randint(1,100)
    print('The random number generated between 1 and 100:', geeb)
    Meck.remove_from_rear()

print(' ')
print('The simulations for the second row')   
if items > 0 and items <= 0.1:
    geeb = random.randint(1,100)
    print('The random number generated between 1 and 100:', geeb)
    Meck.add_to_front(geeb)

if items > 0.1 and items <= 0.7:
    geeb = random.randint(1,100)
    print('The random number generated between 1 and 100:', geeb)
    Meck.remove_from_front()
    
if items > 0.7 and items <= 0.8:
    geeb = random.randint(1,100)
    print('The random number generated between 1 and 100:', geeb)
    Meck.add_to_rear(geeb)
    
if items > 0.8 and items <= 1:
    geeb = random.randint(1,100)
    print('The random number generated between 1 and 100:', geeb)
    Meck.remove_from_rear()
    
print(' ')
print('After running the code: ')
print('The items in the array: ', Meck.display_items())
print('Is the array empty?', Meck.isEmpty())
print('Is the array full?', Meck.isFull())
print('What is the size of the array?', Meck.size())

'''
The cummulative interval was generated from the table given. If the generated number from items falls
within a particular range, the method is called and the function is performed by either adding or removing
the geeb to the front or rear of the array
The array is displayed, checked if it is full or empty and the size is noted before and after the code is run
'''
# All possible cases have been tested to ensure the effective run of the code