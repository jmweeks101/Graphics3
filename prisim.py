from graphics import *
import numpy as np
import math

def BasePoints(baseCenter,baseSides,height,width):
    basePoints = []
    #find starting angle from interior angle measurment of base shape
    anglei = np.radians(180-((baseSides-2)*180/baseSides))
    #if base has odd sides
    if baseSides % 2 == 0:
        angle = anglei/2
    else:
        angle = np.radians(90)
    #find first point of the base by using half the interior angle and the center
    x = baseCenter.getX()+np.cos(angle)*width/2
    y = baseCenter.getY()+np.sin(angle)*height/2
    basePoints.append(Point(x,y))
    #find rmeinaing points by moving one angle measuremnt around until you have all points
    for i in range(baseSides-1):
        angle += anglei
        x = baseCenter.getX()+np.cos(angle)*width/2
        y = baseCenter.getY()+np.sin(angle)*height/2
        basePoints.append(Point(x,y))
    return basePoints

def PrisimPoints(baseCenter,baseSides,height,width,depth,angle):
    #creat eempty list to store faces in
    faces = []
    basePoints = BasePoints(baseCenter,baseSides,height,width)
    #add the base to faces
    faces.append(Polygon(basePoints))
    #dictionary for points that will be used to make faces
    #work your way around the shape from there, clockwise
    #dictionaries will differ for even and odd sided base shapes
    quadOdd = {0:list(range(int(math.floor((baseSides+3)/8)),-1,-1))+list(range(baseSides-1,int((math.floor((baseSides-3)/6)+(baseSides-3)/2+2))-1,-1)),
               1:list(range(int((math.floor((baseSides-3)/6)+(baseSides-3)/2+2))-1,-1,-1))+list(range(baseSides-1,baseSides-int(math.floor((baseSides+3)/8))-1,-1)),
               2:list(range(int(math.floor((baseSides+3)/8)),-1,-1))+list(range(baseSides-1,int((math.floor((baseSides-3)/6)+(baseSides-3)/2+2))-1,-1)),
               3:list(range(int(math.floor((baseSides+3)/8)),-1,-1))+list(range(baseSides-1,int((math.floor((baseSides-3)/6)+(baseSides-3)/2+2))-1,-1))}
    quadEven = {0:[],1:[],2:[],3:[]}
    if baseSides % 2 == 0:
        points = quadEven[angle//np.radians(90)]
    else:
        points = quadOdd[angle//np.radians(90)]
    print(points)
    for i in range(len(points)-1):
        p1 = basePoints[points[i]]
        p2 = basePoints[points[i+1]]
        faces.append(Polygon(p1,p2,Point(p2.getX()+depth*np.cos(angle),p2.getY()+depth*np.sin(angle)),Point(p1.getX()+depth*np.cos(angle),p1.getY()+depth*np.sin(angle))))
    return faces

def test():
    win = GraphWin("",500,500)
    win.setCoords(0,0,10,10)
    while True:
        sides = int(input("Base Sides: "))
        angle = int(input("Angle: "))
        faces = PrisimPoints(Point(5,5),sides,4,4,3,np.radians(angle))
        for face in faces:
            face.draw(win)
        win.getMouse()
        for face in faces:
            face.undraw()
    win.close()

test()
