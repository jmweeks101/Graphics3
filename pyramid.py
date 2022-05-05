#allows the user to create pyramids of a specified base
import numpy as np
from graphics import *
#function to generate points of the pyramid
#takes the apex of the pyramid as 'tip'
#also takes the height and the number of sides on the base shape, and the length of those sides
def PyramidPoints(tip, height, baseSides, sideLength):
    #finds the center of the 2D view of the base
    #all remnaing points are found from this point and the apex
    center = Point(tip.getX(), tip.getY()-height)
    #if the base shape has an even amount of sides...
    if baseSides % 2 == 0:
        p1 = center
        #find the angle from the center point to the next point
        angle = (((baseSides-2)*180)/baseSides)/2
        #points will be saved in lists seperated by left and right of the center point
        leftPoints = [p1]
        rightPoints = [p1]
        #create the middle line from apex to base center
        middle = Line(tip,center)
        #goes through loop n amount of times neccessary to find all visible faces
        #finds a right and left point each loop
        for i in range(int((baseSides/2)-1)):
            rightPoints.append(Point(rightPoints[-1].getX()+np.cos(angle)*sideLength, rightPoints[-1].getY()+np.sin(angle)*sideLength))
            leftPoints.append(Point(leftPoints[-1].getX()-np.cos(angle)*sideLength, leftPoints[-1].getY()+np.sin(angle)*sideLength))
    #if the base shape has an odd amount of sides...
    else:
        p1 = Point(center.getX()-(sideLength/2), center.getY())
        p2 = Point(center.getX()+(sideLength/2), center.getY())
        angle = (((baseSides-2)*180)/baseSides)/2
        leftPoints = [p1]
        rightPoints = [p2]
        middle = None
        for i in range(baseSides//2 - 1):
            leftPoints.append(Point(leftPoints[-1].getX()+np.cos(angle)*sideLength, leftPoints[-1].getY()+np.sin(angle)*sideLength))
            rightPoints.append(Point(rightPoints[-1].getX()-np.cos(angle)*sideLength, rightPoints[-1].getY()+np.sin(angle)*sideLength))
    #return points and middle line
    return leftPoints,rightPoints,middle

def drawPyramid(tip, height, baseSides, sideLength):
    leftPoints,rightPoints,middle = PyramidPoints(tip, height, baseSides, sideLength)
    faces = []
    if middle==None:
        for i in range(len(leftPoints)-1):
            faces.append(Polygon(tip,leftPoints[i],leftPoints[i+1]))
            faces.append(Polygon(tip,rightPoints[i],rightPoints[i+1]))
    else:
        faces.append(middle)
        for i in range(len(leftPoints)-1):
            faces.append(Polygon(tip,leftPoints[i],leftPoints[i+1]))
            faces.append(Polygon(tip,rightPoints[i],rightPoints[i+1]))
    return faces

def main():
    win = GraphWin('', 500, 500)
    win.setCoords(0,0,10,10)

    faces = drawPyramid(Point(5,8),4,4,2)
    for face in faces:
        face.draw(win)

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
