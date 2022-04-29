from parallelogram import create3
from pyramid import *
import numpy as np

#base shape class, will define all 3d shape subclasses
class base3D:
    #user gives base shape and dimensions to contain 3D shape
    def __init__(self,win,faces):
        self.win = win
        self.faces = faces
        self.fillColor = None
        self.edgeColor = None
        self.edgeSize = None
        self.points = []
        #go through each face
        for face in self.faces:
            #find each point in each face
            try:
                self.points = self.points + face.getPoints()
            #for when there is a line in self.faces
            except:
                self.points = self.points + [face.getCenter()]

    #update self.points
    def updatePoints(self):
        self.points = []
        #go through each face
        for face in self.faces:
            #find each point in each face
            try:
                self.points = self.points + face.getPoints()
            #for when there is a line in self.faces
            except:
                self.points = self.points + [face.getCenter()]

    #returns cnter of the object
    def getCenter(self):
        points = []
        xList = []
        yList = []
        #take out duplicate points
        points2 = []
        for point in self.points:
            if point not in points2:
                points2.append(point)
        #put the x and y coordinates of each point in seperate lists
        for point in points2:
            xList.append(point.getX())
            yList.append(point.getY())
        #retiurn the center by taking the average of the two lists
        return Point(sum(xList)/len(xList),sum(yList)/len(yList))

    #translate shape in x,y direction
    def translate(self,x,y):
        self.undrawLabel()
        for face in self.faces:
            face.move(x,y)
        self.updatePoints()

    #makes pbject apear closer or further away(shrink or grow shape)
    def zoom(self,z):
        self.undrawLabel()
        #find the current center and undraw current shape
        center = self.getCenter()
        self.hide()
        #list to store new faces
        faces2 = []
        for face in self.faces:
            points = face.getPoints()
            points2 = []
            for point in points:
                #for each point in each face, find the relative position to the center in x and y
                if point.getX()-center.getX()>0:
                    x = 1
                else:
                    x = -1
                if point.getY()-center.getY()>0:
                    y = 1
                else:
                    y = -1
                #create a new point that is zoomed in/out from the original
                points2.append(Point(point.getX()+z*np.cos(np.radians(45))*x,point.getY()+z*np.sin(np.radians(45))*y))
            faces2.append(Polygon(points2))
        #save new faces to self.faces
        self.faces = faces2
        #add back customizations if any
        try:
            self.fill(self.fillColor)
        except:
            pass
        try:
            self.setEdgeSize(self.edgeSize)
        except:
            pass
        try:
            self.setEdgeColor(self.edgeColor)
        except:
            pass
        self.show()
        self.updatePoints()

    #rotate the object in 3D space
    def rotate(self,thetaX,thetaY,thetaZ):
        self.undrawLabel()
        pass
        self.updatePoints()

    #draw shape to window
    def show(self):
        for face in self.faces:
            face.draw(self.win)

    #undraw shape from window
    def hide(self):
        self.undrawLabel()
        for face in self.faces:
            face.undraw()

    #set fill color for shape
    def fill(self,color):
        for face in self.faces:
            face.setFill(color)
        self.fillColor = color

    #set edge color
    def setEdgeColor(self,color):
        for face in self.faces:
            face.setOutline(color)
        self.edgeColor = color

    #set edge pixel width
    def setEdgeSize(self,size):
        for face in self.faces:
            face.setWidth(size)
        self.edgeSize = size

    #customize label
    def setLabel(self,text,color,size,x,y):
        self.label = Text(self.getCenter(),text)
        self.label.setTextColor(color)
        self.label.setSize(size)
        self.label.move(x,y)

    #displays a label custom label over shape
    def drawLabel(self):
        try:
            self.label.draw(self.win)
        except:
            pass

    #undraws label
    def undrawLabel(self):
        try:
            self.label.undraw()
        except:
            pass

#class to create a prisim
class Prisim(base3D):
    def __init__(self,win,baseCenter,height,width,depth):
        self.win = win
        self.baseCenter = baseCenter
        self.width = width
        self.height = height
        self.depth = depth
        #create base shape
        base3D.__init__(self,self.win,create3(self.depth,self.width,self.height,self.baseCenter))

    #returns a clone of the prisim
    def clone(self):
        return Prisim(self.win,self.baseCenter,self.height,self.width,self.depth)

#class to create a pyramid
class Pyramid(base3D):
    def __init__(self,win,tip,height,baseSides,sideLength):
        self.win = win
        self.tip = tip
        self.height = height
        self.baseSides = baseSides
        self.sideLength = sideLength
        #create base shape
        base3D.__init__(self,self.win,makePyramid(self.tip, self.height, self.baseSides, self.sideLength))

    #returns a clone of the prisim
    def clone(self):
        return Pyramid(self.win,self.tip,self.height,self.baseSides,self.sideLength)

#class to create a sphere
class Sphere(base3D):
    def __init__(self):
        pass
