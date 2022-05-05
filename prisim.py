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

def PrisimFaces(baseCenter,baseSides,height,width,depth,angle):
    #creat eempty list to store faces in
    faces = []
    basePoints = BasePoints(baseCenter,baseSides,height,width)
    #add the base to faces
    faces.append(Polygon(basePoints))
    #find angle to rotate points against
    refAngle = np.radians(90-angle)
    #rotation matrix
    matrix = np.array([[np.cos(refAngle),-np.sin(refAngle)],
                      [np.sin(refAngle),np.cos(refAngle)]])
    #rotate each base point and save it to a new list
    basePointsR = []
    for point in basePoints:
        pointA = np.array([[point.getX()-baseCenter.getX()],
                          [point.getY()-baseCenter.getY()]])
        pointR = np.matmul(matrix,pointA)
        basePointsR.append(Point(pointR[0]+baseCenter.getX(),pointR[1]+baseCenter.getY()))
    #with rotated points list, find the point with the smallest x value
    xList = []
    for point in basePointsR:
        xList.append(point.getX())
    #establish starting point
    start = xList.index(min(xList))
    #make first face
    faces.append(makeFace(basePoints[start],basePoints[start-1],depth,angle))
    i = start
    while basePointsR[i-1].getX()>basePointsR[i].getX():
        faces.append(makeFace(basePoints[i],basePoints[i-1],depth,angle))
        i -= 1
    return faces

#create a new face
def makeFace(p1,p2,depth,angle):
    return Polygon(p1,p2,Point(p2.getX()+depth*np.cos(np.radians(angle)),p2.getY()+depth*np.sin(np.radians(angle))),Point(p1.getX()+depth*np.cos(np.radians(angle)),p1.getY()+depth*np.sin(np.radians(angle))))
