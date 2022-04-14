from rhombus import Rhombus
from 2Drotation import *

#base shape class, will define all 3d shape subclasses
class base3D:
    #user gives center point and dimensions to contain 3D shape
    def __init__(win,center,height,width,depth):
        self.win = win
        self.center = center
        self.height = height
        self.width = width
        self.depth = depth
        #faces list will contain 2D shapes
        self.faces = []

    #translate shape in x,y direction
    def translate(self,x,y):
        pass

    #draw shape to window
    def show(self):
        for face in self.faces:
            face.draw(self.win)

    #undraw shape from window
    def hide(self):
        for face in self.faces:
            face.undraw()

#class to create a cube
class Cube(base3D):
    def __init__(self):
        pass


    #makes shape into a sphere
class Sphere(base3D):
    def __init__(self):
