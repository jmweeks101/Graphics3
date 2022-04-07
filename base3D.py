import sys
sys.path.insert(0, 'C:\\Users\\joshm\\OneDrive\\Documents\\Computer Science')
from graphics import *

#base shape class, will define all 3d shape subclasses
class base3D():
    #user gives center point and dimensions to contain 3D shape
    def __init__(center,height,width,depth):
        self.center = center
        self.height = height
        self.width = width
        self.depth = depth

    #returns center point
    def getCenter(self):
        return self.center

    #translate shape in x,y direction
    def translate(self,x,y):
        pass

    #makes shape into a cube
    def setCube(self):
        pass

    #makes shape into a sphere
    def setSphere(self):
        pass
