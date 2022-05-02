from graphics import *
from base3D import *
import numpy as np

def main():
    win = GraphWin("Graphics3",900,900)
    win.setCoords(0,0,10,10)
    cube = Prisim(win,Point(8,4),2,2,2)
    cube.show()
    win.getMouse()
    cube.rotate(np.radians(90),0,0)
    win.getMouse()
    win.close()

def allPyramids(win):
    win.setCoords(0,0,40,40)
    shapes = []
    labels = []
    for i in range(12):
        shapes.append(Pyramid(win,Point(((i%4)+1)*8,((i//4)+1)*12),8,i+3,2))
        labels.append(Text(Point(((i%4)+1)*8,((i//4)+1)*12-10),i+3))
    for i in range(12):
        shapes[i].show()
        labels[i].draw(win)
    win.getMouse()
    for shape in shapes:
        shape.zoom(5)
    win.getMouse()

def testShape(win,shape):
    win.setCoords(0,0,10,10)
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

if __name__ == "__main__":
    main()
