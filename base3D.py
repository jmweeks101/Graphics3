from rhombus import Rhombus
from rotation2D import *

#base shape class, will define all 3d shape subclasses
class base3D:
    #user gives base shape and dimensions to contain 3D shape
    def __init__(win,base,width,height,depth):
        self.win = win
        self.base = base
        self.x = x
        self.y = y
        self.z = z
        #faces list will contain 2D shapes
        self.faces = [base]

    #returns enter of object
    def getCenter(self):
        pass

    #translate shape in x,y direction
    def translate(self,x,y):
        for face in self.faces:
            face.move(x,y)

    #makes pbject apear closer or further away(shrink or grow shape)
    def zoom(self,z):
        pass

    #returns a clone of the 3D shape
    def clone(self):
        return base3D(self.win,self.base.clone(),self.x,self.y,self.z)

    #draw shape to window
    def show(self):
        for face in self.faces:
            face.draw(self.win)

    #undraw shape from window
    def hide(self):
        for face in self.faces:
            face.undraw()

    #set fill color for shape
    def fill(self,color):
        for face in self.faces:
            face.setFill(color)

    #set edge color
    def edgeColor(self,color):
        for face in self.faces:
            face.setOutline(color)

    #set edge pixel width
    def edgeSize(self,size):
        for face in self.faces:
            face.setWidth(size)

    #displays a label custom label over shape
    def drawLabel(self,text,color,size):
        self.label = Text(self.getCenter(),text)
        self.label.setTextColor(color)
        self.label.setTextSize(size)
        self.draw(self.win)

    #undraws label
    def undrawLabel(self):
        self.label.undraw()

#class to create a prisim from base 2D shape
class Prisim(base3D):
    def __init__(self):
        pass

#class to create a pyramid from base 2D shape
class Pyramid(base3D):
    def __init__(self):
        pass

#class to create a sphere
class Sphere(base3D):
    def __init__(self):
        pass
