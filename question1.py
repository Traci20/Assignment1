'''
Name : Traci Ewurabena Nhyira Gyebi
ID : 37242022
Assignment 2
'''
'''
Brief Introdcution of the Code: - This is the class deque that adds data from the front and rear as
well as removes data from the front and rear. The class deﬁnes and implements other auxiliary functions
for instance object creation, determining the size, i.e., number of elements in the deque, whether the
deque is empty or not and also whether it is full or not. 
'''
# Random - Helps in generating random numbers
import random

class Deque:
# Constructor methodd
    def __init__(self):
        self.items = []
        
# This add_to_front method inserts data at index 0 when called
    def add_to_front(self, data):
        self.items.insert(0, data)

# This add_to_rear method appends data to index -1 when called
    def add_to_rear(self, data):
        self.items.append(data)

# This remove_from_front method pops data 
    def remove_from_front(self):
        if self.items == []:
            return "Cannot remove array is empty"
        else:
            self.items.pop(0)

# This remove_from_rear method pops data
    def remove_from_rear(self):
        if self.items == []:
            return "Cannot remove array is empty"
        else:
            self.items.pop()

# This method returns an empty list if its empty
    def isEmpty(self):
        return self.items == []

# This method returns 20 if the list is full
    def isFull(self):
        return len(self.items) == 20

# This method returns an empty list if the array is null and returns the length of the array if its not
    def size(self):
        if self.items == []:
            return "Array is null"
        else:
            return len(self.items)

# This method returns the data at index 0
    def top_front(self):
        return self.items[0]

# This method returns the data at index -1
    def top_back(self):
        return self.items[-1]

# This method displays the items in the array
    def display_items(self):
        return self.items