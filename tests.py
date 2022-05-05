#This file contains a sequence that displays the three different shapes we created
#As well as displaying some of the methods we created.

from graphics import *
from base3D import *
import numpy as np

def testShape(win,shape):
    shape.show()
    win.getMouse()
    # fill color
    shape.fill("blue")
    win.getMouse()
    # move
    shape.translate(-1,1)
    win.getMouse()
    #make label
    shape.setLabel("Our shape","red",20,0,0)
    shape.drawLabel()
    win.getMouse()
    #customize edges
    shape.setEdgeColor("green")
    shape.setEdgeSize(3)
    win.getMouse()
    #clone
    cube2 = shape.clone()
    cube2.translate(2,2)
    cube2.show()
    win.getMouse()
    #zoom
    shape.zoom(2)
    shape.setLabel("Our shape","red",20,0,0)
    shape.drawLabel()
    win.getMouse()

def main():
    win = GraphWin("Graphics3",900,900)
    win.setCoords(0,0,10,10)
    testShape(win, Prisim(win,Point(4,4),5,2,2,2,45))

if __name__ == "__main__":
    main()
