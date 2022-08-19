#This file contains a sequence that displays the three different shapes we created
#As well as displaying some of the methods we created.

from graphics import *
from base3D import *
import numpy as np
from sphere import *

def testShape(win,shape,label):
    shape.show()
    win.getMouse()
    # fill color
    label.setText("Change fill color using: shape.fill(color)")
    shape.fill("blue")
    win.getMouse()
    # move
    label.setText("Move the shape using: shape.translate(x,y)")
    shape.translate(-1,1)
    win.getMouse()
    #make label
    label.setText("Create a label for the shape using: shape.setLabel()")
    shape.setLabel("Our shape","red",20,0,0)
    shape.drawLabel()
    win.getMouse()
    #customize edges
    label.setText("Change edge size and color using:\nshape.setEdgeSize(size) and shape.setEdgeColor(color)")
    shape.setEdgeColor("green")
    shape.setEdgeSize(3)
    win.getMouse()
    #clone
    label.setText("Create a clone of your shape using: shape.clone()")
    cube2 = shape.clone()
    cube2.translate(2,-3)
    cube2.show()
    win.getMouse()
    #zoom
    cube2.hide()
    label.setText("Zoom in or out using: shape.zoom()")
    shape.zoom(2)
    win.getMouse()
    shape.zoom(-1)
    win.getMouse()
    #rotate
    label.setText("Rotate your shape using: shape.rotate()")
    shape.rotate(45,Point(5,5))
    win.getMouse()
    shape.hide()

def main():
    win = GraphWin("Graphics3",900,900)
    win.setCoords(0,0,10,10)
    label = Text(Point(5,9),"")
    label.setSize(24)
    label.draw(win)
    testShape(win, Prisim(win,Point(4,4),5,2,2,2,45), label)
    testShape(win, Pyramid(win, Point(6,6), 4, 5, 2), label)
    label.setText("Create spheres with the sphere object:")
    sphere = Sphere(win, Point(7,7), 1, [100,100,100], side='left')
    sphere2 = Sphere(win, Point(3,3), 1, [100,100,100])
    sphere.createSphere()
    sphere2.createSphere()
    win.getMouse()



if __name__ == "__main__":
    main()
