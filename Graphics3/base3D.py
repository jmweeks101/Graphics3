from prisim import PrisimFaces
from pyramid import *
from sphere import Sphere
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

    #rotate the object in 3D space
    def rotate(self,angle,anchor):
        self.hide()
        self.undrawLabel()
        #rotation matrix
        matrix = np.array([[np.cos(angle),-np.sin(angle)],
                          [np.sin(angle),np.cos(angle)]])
        anchorX = anchor.getX()
        anchorY = anchor.getY()
        #saved new rotated faces to a new list
        faces2 = []
        for face in self.faces:
            points2 = []
            for point in face.getPoints():
                p = np.array([[point.getX()-anchorX],
                             [point.getY()-anchorY]])
                x = np.matmul(matrix,p)
                points2.append(Point(x[0]+anchorX,x[1]+anchorY))
            faces2.append(Polygon(points2))
        self.faces = faces2
        #add back original customizations if any were present
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

#class to create a prisim
class Prisim(base3D):
    def __init__(self,win,baseCenter,baseSides,height,width,depth,angle):
        self.win = win
        self.baseCenter = baseCenter
        self.baseSides = baseSides
        self.width = width
        self.height = height
        self.depth = depth
        if angle < 0:
            angle = abs(angle)
        else:
            if angle >= 360:
                self.angle = angle % 360
            else:
                self.angle = angle
        #create base shape
        base3D.__init__(self,self.win,PrisimFaces(self.baseCenter,self.baseSides,self.height,self.width,self.depth,self.angle))

    #returns a clone of the prisim
    def clone(self):
        return Prisim(self.win,self.baseCenter,self.baseSides,self.height,self.width,self.depth,self.angle)

    #translate shape in x,y direction
    def translate(self,x,y):
        self.undrawLabel()
        for face in self.faces:
            face.move(x,y)
        self.baseCenter = Point(self.baseCenter.getX()+x,self.baseCenter.getY()+y)
        self.updatePoints()

    #makes pbject apear closer or further away(shrink or grow shape)
    def zoom(self,z):
        self.undrawLabel()
        self.hide()
        #list to store new faces
        self.faces = PrisimFaces(self.baseCenter,self.baseSides,self.height+z/2,self.width+z/2,self.width+z/2,self.angle)
        #add back original customizations if any were present
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

    #translate shape in x,y direction
    def translate(self,x,y):
        self.undrawLabel()
        for face in self.faces:
            face.move(x,y)
        self.tip = Point(self.tip.getX()+x,self.tip.getY()+y)
        self.updatePoints()

    #makes object apear closer or further away(shrink or grow shape)
    def zoom(self,z):
        #undraw the current shape
        self.undrawLabel()
        self.hide()
        #make new faces from a recalculted tip,height, and base side length
        #find new tip
        tip2 = Point(self.tip.getX(),self.tip.getY()+z/2)
        #find new hight
        height2 = self.height+z
        #find new base side length
        sideLegth2 = int(self.sideLength*(height2)/self.height)
        self.faces = makePyramid(tip2,height2,self.baseSides,sideLegth2)
        #add back original customizations if any were present
        self.show()
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
        self.updatePoints()
