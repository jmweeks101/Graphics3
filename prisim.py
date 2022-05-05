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
    #find reference point from back base
    ref = Point(baseCenter.getX()+depth*np.cos(np.radians(angle)),baseCenter.getY()+depth*np.sin(np.radians(angle)))
    #find start points on base
    l,h = findHiLo(angle,baseSides,basePoints)
    print(l,h)
    #add first side face
    p1 = basePoints[h]
    p2 = basePoints[l]
    faces.append(Polygon(p1,p2,Point(p2.getX()+depth*np.cos(np.radians(angle)),p2.getY()+depth*np.sin(np.radians(angle))),Point(p1.getX()+depth*np.cos(np.radians(angle)),p1.getY()+depth*np.sin(np.radians(angle)))))
    #starting from the low point, go around the base clockwise making faces, until the next face would be concaved
    while True:
        p1 = basePoints[l]
        p2 = basePoints[l-1]
        faces.append(Polygon(p1,p2,Point(p2.getX()+depth*np.cos(np.radians(angle)),p2.getY()+depth*np.sin(np.radians(angle))),Point(p1.getX()+depth*np.cos(np.radians(angle)),p1.getY()+depth*np.sin(np.radians(angle)))))
        l -= 1
        if abs(basePoints[l].getY()-basePoints[l-1].getY())<(np.tan(np.radians(angle))*abs(basePoints[l].getX()-basePoints[l-1].getX())):
            break
    #starting from the high point, go around the base counter-clcokwise making faces, until the next face would concave
    while True:
        p1 = basePoints[h]
        if h>=baseSides-1:
            p2 = basePoints[0]
        else:
            p2 = basePoints[h+1]
        faces.append(Polygon(p1,p2,Point(p2.getX()+depth*np.cos(np.radians(angle)),p2.getY()+depth*np.sin(np.radians(angle))),Point(p1.getX()+depth*np.cos(np.radians(angle)),p1.getY()+depth*np.sin(np.radians(angle)))))
        if h==baseSides-1:
            h = 0
        else:
            h += 1
        if h>=baseSides-1:
            if abs(basePoints[h].getY()-basePoints[0].getY())>(np.tan(np.radians(angle))*abs(basePoints[h].getX()-basePoints[0].getX())):
                break
        else:
            if abs(basePoints[h].getY()-basePoints[h+1].getY())>(np.tan(np.radians(angle))*abs(basePoints[h].getX()-basePoints[h+1].getX())):
                break
    return faces

def findHiLo(angle,baseSides,basePoints):
    #find two starting points from base
    if angle>90:
        theta = angle-90
    else:
        theta = 360-angle
    j = math.floor(theta/(180-(baseSides-2)*180/baseSides))
    low = j
    if j==baseSides-1:
        high = 0
    else:
        high = j+1
    return low,high

def test():
    win = GraphWin("",500,500)
    win.setCoords(0,0,10,10)
    while True:
        sides = int(input("Base Sides: "))
        angle = int(input("Angle: "))
        faces = PrisimPoints(Point(5,5),sides,4.5,4.5,3,angle)
        for face in faces:
            face.draw(win)
        win.getMouse()
        for face in faces:
            face.undraw()
    win.close()

test()
