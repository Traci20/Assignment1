'''
Name : Traci Ewurabena Nhyira Gyebi
ID : 37242022
Assignment 2
'''
'''
This is the test file for the Binary Search
'''
from question2a import *

# gea serves as an empty list which will store the average time it took to run the code five times
gea = []
print('When the range size for the random numbers is 100: ')
N = 100
print(' ')
for i in range(5):
    start = time.time()
    testlist = random.sample(range(1,32767),N)
    ads = sorted(testlist)
    print('The sorted list for the random numbers: ', ads)
    print(' ')
    it = int(input('Please enter a number: '))
    print('The number is found in the list: ', binarySearch(ads, it))
    print(' ')
    end = time.time()
    gent = (end - start)*1000
    print('The time it took to run the code is', gent, 'msec')
    print(' ')
    gea.append(gent)
print('The average time it took to run the code five times is:', sum(gea)/5, 'msec')
print(' ')

gea = []
print('When the range size for the random numbers is 1000: ')
N = 1000
for i in range(5):
    start = time.time()
    testlist = random.sample(range(1,32767),N)
    ads = sorted(testlist)
    print('The sorted list for the random numbers: ', ads)
    print(' ')
    it = int(input('Please enter a number: '))
    print('The number is found in the list: ', binarySearch(ads,it))
    print(' ')
    end = time.time()
    gent = (end - start)*1000
    print('The time it took to run the code is', gent, 'msec')
    print(' ')
    gea.append(gent)
print('The average time it took to run the code five times is:', sum(gea)/5, 'msec')
print(' ')

gea = []
print('When the range size for the random numbers is 5000: ')
N = 5000
for i in range(5):
    start = time.time()
    testlist = random.sample(range(1,32767),N)
    ads = sorted(testlist)
    print('The sorted list for the random numbers: ', ads)
    print(' ')
    it = int(input('Please enter a number: '))
    print('The number is found in the list: ', binarySearch(ads,it))
    print(' ')
    end = time.time()
    gent = (end - start)*1000
    print('The time it took to run the code is', gent, 'msec')
    print(' ')
    gea.append(gent)
print('The average time it took to run the code five times is:', sum(gea)/5, 'msec')
print(' ')

'''
This test file generates random numbers between 1-32767 with a variety of sizes(100,1000,500). Then it sorts  
the list out, asks the user for a number to be searched for. It then identifies if the number is in the array
or not. Calculates the time it took to run the code. Then finally calculates the average time it took to calculate
the code five times.
'''
# All possible cases have been tested to ensure the effective run of the code