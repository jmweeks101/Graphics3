#Function designed to be able to rotate shapes on the 2D plane. This will
#allow us to manipulate the shapes in order to make them appear 3D.
import sys
sys.path.insert(0, 'C:\\Users\\joshm\\OneDrive\\Documents\\Computer Science')
from graphics import *
import numpy as np
from rhombus import Rhombus

def rotate(shape, degrees):
    degrees = np.radians(degrees)
    pivotx, pivoty =  shape.p1.x + ((shape.p2.x-shape.p1.x)/2), shape.p1.y + ((shape.p2.y-shape.p1.y)/2)
    p1 = np.matrix([[shape.p1.x-pivotx], [shape.p1.y-pivoty]])
    p2 = np.matrix([[shape.p2.x-pivotx], [shape.p2.y-pivoty]])
    matrix = np.matrix([[np.cos(degrees), -np.sin(degrees)], [np.sin(degrees), np.cos(degrees)]])
    newp1 = np.matmul(matrix, p1)
    newp2 = np.matmul(matrix, p2)
    shape.p1.x, shape.p1.y = newp1[0,0]+pivotx, newp1[1,0]+pivoty
    shape.p2.x, shape.p2.y = newp2[0,0]+pivotx, newp2[1,0]+pivoty

def main():
    win = GraphWin('GraphicsGroup', 600,600)
    win.setBackground('white')
    win.setCoords(0,0,10,10)

    test = Rectangle(Point(3,3), Point(6,7))
    rotate(test,0)

    test.draw(win)

    win.getMouse()

if __name__ == '__main__':
    main()
