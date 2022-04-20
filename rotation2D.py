#Function designed to be able to rotate shapes on the 2D plane. This will
#allow us to manipulate the shapes in order to make them appear 3D.
import sys
sys.path.insert(0, 'C:\\Users\\joshm\\OneDrive\\Documents\\Computer Science')
from graphics import *
import numpy as np
from rhombus import Rhombus

def rotateRect(shape, degrees):
    p3 = Point(shape.p1.x, shape.p2.y)
    p4 = Point(shape.p2.x, shape.p1.y)
    points = [p1, p4, p2, p3]
    degrees = np.radians(degrees)
    pivotx, pivoty =  shape.p1.x + ((shape.p2.x-shape.p1.x)/2), shape.p1.y + ((shape.p2.y-shape.p1.y)/2)
    newpoints = []
    for p in points:
        p = np.matrix([[p.getX()-pivotx], [p.getY()-pivoty]])
        matrix = np.matrix([[np.cos(degrees), -np.sin(degrees)], [np.sin(degrees), np.cos(degrees)]])
        newp = np.matmul(matrix, p)
        newpoints.append(newp[0,0]+pivotx, newp[1,0]+pivoty)
    shape = Polygon(newpoints)
    return shape


def main():
    win = GraphWin('GraphicsGroup', 600,600)
    win.setBackground('white')
    win.setCoords(0,0,10,10)

    test = Rectangle(Point(3,3), Point(6,7))
    test = rotate(test,40)

    test.draw(win)

    win.getMouse()

if __name__ == '__main__':
    main()
