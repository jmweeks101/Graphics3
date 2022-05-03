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
    #find what the center of the back face would be
    backCenter = Point(baseCenter.getX()+depth*np.cos(angle),baseCenter.getY()+depth*np.sin(angle))
    #find which point of the base is closest to this back point
    dist = []
    for point in basePoints:
        x1 = point.getX()
        x2 = backCenter.getX()
        y1 = point.getY()
        y2 = backCenter.getY()
        dist.append(np.sqrt((x1-x2)**2+(y1-y2)**2))
    print(dist)
    distSort = dist.copy()
    distSort.sort(reverse = True)
    #use the cloest point and the adjust points to it on the base to make the side faces
    for i in range(baseSides):
        if distSort.index(dist[i]) >= math.floor(baseSides/2):
            p1 = basePoints[i]
            if i+1 > len(basePoints)-1:
                p2 = basePoints[0]
            else:
                p2 = basePoints[i+1]
            faces.append(Polygon(p1,p2,Point(p2.getX()+depth*np.cos(angle),p2.getY()+depth*np.sin(angle)),Point(p1.getX()+depth*np.cos(angle),p1.getY()+depth*np.sin(angle))))
    return faces

def test():
    win = GraphWin("",500,500)
    win.setCoords(0,0,10,10)
    faces = PrisimPoints(Point(5,5),7,2,2,3,np.radians(45))
    for face in faces:
        face.draw(win)
    win.getMouse()
    win.close()

test()
