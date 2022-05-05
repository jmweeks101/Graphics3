from parallelogram import create3
from prisim import PrisimFaces
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
    def __init__(self,win,baseCenter,baseSides,height,width,depth,angle):
        self.win = win
        self.baseCenter = baseCenter
        self.baseSides = baseSides
        self.width = width
        self.height = height
        self.depth = depth
        if angle < 0:
            angle = abs(angle)
            if angle >= 360:
                self.angle = angle % 360
            else:
                self.angle = angle
        #create base shape
        base3D.__init__(self,self.win,PrisimFaces(self.baseCenter,self.baseSides,self.height,self.width,self.depth,self.angle))

    #returns a clone of the prisim
    def clone(self):
        return Prisim(self.win,self.baseCenter,self.height,self.width,self.depth)

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
            #find each point in the face
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
                #create a new point that is n distance from the original point
                #distance n is calculated by using given scale amount (z) as a diagnol distance from the point, away from the center
                points2.append(Point(point.getX()+z*np.cos(np.radians(45))*x,point.getY()+z*np.sin(np.radians(45))*y))
            #new points are formed into new faces and saved to self.faces
            faces2.append(Polygon(points2))
        #save new faces to self.faces
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
        self.tip.move(x,y)
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

    #rotate the object in 3D space
    def rotate(self,angleX,angleY,angleZ):
        self.hide()
        angleX = angleX/2
        angleY = angleY/2
        angleZ = angleZ/2
        #rotation matrix X
        matrixX = np.array([[1,         0,             0      ],
                            [0, np.cos(angleX), np.sin(angleX)],
                            [0, -np.sin(angleX), np.cos(angleX)]])
        #rotation matrix Y
        matrixY = np.array([[np.cos(angleY), 0, -np.sin(angleY)],
                            [0,              1,        0       ],
                            [np.sin(angleY), 0, np.cos(angleY)]])
        #rotation matrix Z
        matrixZ = np.array([[np.cos(angleZ), np.sin(angleZ), 0 ],
                            [-np.sin(angleZ),np.cos(angleZ), 0 ],
                            [      0        ,      0      ,  1 ]])
        #function to rotate in a single direction
        def rotate1(faces,angle,matrix):
            #list to save new rotated faces
            faces2 = []
            for face in faces:
                points = face.getPoints()
                points2 = []
                for point in points:
                    #save face points in a matrix
                    pointMatrix = np.array([point.getX(),point.getY()])
                    product = np.matmul(pointMatrix,matrix)
                    points2.append(Point(product[0],product[1]))
                faces2.append(Polygon(points2))
            return faces2
        #rotate in each direction
        if angleX is not 0:
            self.faces = rotate1(self.faces,angleX,matrixX)
        if angleY is not 0:
            self.faces = rotate1(self.faces,angleY,matrixY)
        if angleZ is not 0:
            self.faces = rotate1(self.faces,angleZ,matrixZ)
        #draw new shape
        self.show()
#class to create a sphere
class Sphere(base3D):
    def __init__(self):
        pass
