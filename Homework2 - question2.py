'''
Name - Traci Ewurabena Nhyira Gyebi
ID - 37242022

This function calculates the area and perimeter of a given set of coordinates
It also checks for intersection when more than two rectangles are identified

'''
import math
# The math library is a package that allows users to perform any mathematical formula at all

class Point():
    def __init__(self, x1=0, y1=0):
        self.x1 = x1
        self.y1 = y1
        
    def get_x1(self):
        return self.x1
    
    def get_y1(self):
        return self.y1

class Rectangle():
    def __init__(self, BottomLeft, TopRight):
        self.BottomLeft = BottomLeft
        self.TopRight = TopRight
    
    def get_BottomLeft(self):
        return self.BottomLeft
    
    def get_TopRight(self):
        return self.TopRight
        
    def Area(self):
        length = (self.TopRight[0] - self.BottomLeft[0])
        width = (self.TopRight[1] - self.BottomLeft[1])
        return length * width
    
    def Perimeter(self):
        length = (self.TopRight[0] - self.BottomLeft[0])
        width = (self.TopRight[1] - self.BottomLeft[1])
        return 2*(length + width)
    
# This function calculates the area & perimeter
# of the rectangle and also goes ahead to find out if the rectangles are intersecting

def OverLap():
    TopRight = Point()
    TopRightX = int(input("Please enter the X component for the Top Right Corner: "))
    TopRightY = int(input("Please enter the Y component for the Top Right Corner: "))
        
    BottomLeft = Point()
    BottomLeftX = int(input("Please enter the X component for the Bottom Left Corner: "))
    BottomLeftY = int(input("Please enter the Y component for the Bottom Left Corner: "))

    TopRightn = Point()
    TopRightXn = int(input("Please enter the X component for the Top Right Corner: "))
    TopRightYn = int(input("Please enter the Y component for the Top Right Corner: "))
        
    BottomLeftn = Point()
    BottomLeftXn = int(input("Please enter the X component for the Bottom Left Corner: "))
    BottomLeftYn = int(input("Please enter the Y component for the Bottom Left Corner: "))
        
            
    if (BottomLeftX > TopRightXn and BottomLeftXn > TopRightX):
        return False
    if (BottomLeftY < TopRightYn and BottomLeftYn < TopRightY):
        return False
    return True
        
        
rectangle1 = Rectangle((5,5),(30,20))
print("The area of the rectangle is: ",rectangle1.Area())
print("The perimeter of the rectangle is: ",rectangle1.Perimeter())
print("The rectangles are intersecting: ", OverLap())


    
    








    



    
