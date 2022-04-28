from parallelogram import create3
from pyramid import makePyramid

#base shape class, will define all 3d shape subclasses
class base3D:
    #user gives base shape and dimensions to contain 3D shape
    def __init__(self,win,faces):
        self.win = win
        self.faces = faces

    #returns enter of object
    def getCenter(self):
        #take center of each face and make a polygon from those points
        #then find center of that new polygon
        ps = []
        for face in self.faces:
            ps.append(face.getCenter())
        x = Polygon(ps)
        return x.getCenter()

    #translate shape in x,y direction
    def translate(self,x,y):
        self.undrawLabel()
        for face in self.faces:
            face.move(x,y)

    #makes pbject apear closer or further away(shrink or grow shape)
    def zoom(self,z):
        self.undrawLabel()
        pass

    #rotate the object in 3D space
    def rotate(self,thetaX,thetaY,thetaZ):
        self.undrawLabel()
        pass

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
        try:
            self.label.undraw()
        except:
            pass

#class to create a prisim
class Prisim(base3D):
    def __init__(self,win,baseCenter,width,height,depth):
        self.win = win
        self.baseCenter = baseCenter
        self.width = width
        self.height = height
        self.depth = depth
        #create base shape
        base3D.__init__(self,self.win,create3(self.depth,self.width,self.height,self.baseCenter))

    #returns a clone of the prisim
    def clone(self):
        return Prisim(self.win,self.baseCenter,self.width,self.height,self.depth)

#class to create a pyramid
class Pyramid(base3D):
    def __init__(self,win,tip,height,baseSides,baseSideLength):
        self.win = win
        self.tip = tip
        self.height = height
        self.baseSides = baseSides
        self.baseSideLength = baseSideLength
        #create base shape
        base3D.__init__(self,self.win,makePryamid())

#class to create a sphere
class Sphere(base3D):
    def __init__(self):
        pass
