from rhombus import Rhombus
from rotation2D import *

#base shape class, will define all 3d shape subclasses
class base3D:
    #user gives base shape and dimensions to contain 3D shape
    def __init__(win,base,x,y,z):
        self.win = win
        self.base = base
        self.width = x
        self.height = y
        self.depth = z
        #faces list will contain 2D shapes
        self.faces = [base]

    #translate shape in x,y direction
    def translate(self,x,y):
        for face in self.faces:
            face.move(x,y)

    #makes pbject apear closer or further away(shrink or grow shape)
    def zoom(self,z):
        pass

    #draw shape to window
    def show(self):
        for face in self.faces:
            face.draw(self.win)

    #undraw shape from window
    def hide(self):
        for face in self.faces:
            face.undraw()

#class to create a prisim from base 2D shape
class Prisim(base3D):
    def __init__(self):
        pass

#class to create a pyramid from base 2D shape
class Pyramid(base3D):
    def __init__(self):
        pass
