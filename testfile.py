from Homework2 import *

'''
This test file allows the code in the function file to run
The N represents the size, which is the total number of integers requested for
ListA & ListB are a range of random values between 1 & 1000
'''

N = 10
ListA = random.sample(range(1,1000),N)
ListB = random.sample(range(1,1000),N)
DotProduct(N, ListA, ListB)

N = 100
ListA = random.sample(range(1,1000),N)
ListB = random.sample(range(1,1000),N)
DotProduct(N, ListA, ListB)



