#allows the user to create pyramids of a specified base
import numpy as np
from graphics import *
def PyramidPoints(tip, height, baseSides, sideLength):
    center = Point(tip.getX(), tip.getY()-height)
    if baseSides % 2 == 0:
        p1 = center
        angle = (((baseSides-2)*180)/baseSides)/2
        leftpoints = []
        centerpoints = [p1]
        rightpoints = []
        for i in range(int((baseSides/2)-1)):
            points.append([Point(points[i].getX()+np.cos(angle)*sideLength, points[i].getY()+np.sin(angle)*sideLength),
                        Point(points[i].getX()-np.cos(angle)*sideLength, points[i].getY()+np.sin(angle)*sideLength)])
        points = leftpoints + centerpoints + rightpoints
    else:
        p1 = Point(center.getX()-(sideLength/2), center.getY())
        p2 = Point(center.getX()+(sideLength/2), center.getY())
        angle = (((baseSides-2)*180)/baseSides)/2
        points = [p1, p2]
        for i in range(baseSides//2 - 1):
            points.append(Point(points[-2].getX()+np.cos(angle)*sideLength, points[-2].getY()+np.sin(angle)*sideLength))
            points.append(Point(points[-2].getX()-np.cos(angle)*sideLength, points[-2].getY()+np.sin(angle)*sideLength))
        points.insert(0, tip)
    return points

def drawPoints(points):
    for point in


def main():
    win = GraphWin('', 500, 500)
    win.setCoords(0,0,10,10)

    points = PyramidPoints(Point(5,5), 5, 5, 1)
    print(points)

if __name__ == '__main__':
    main()
