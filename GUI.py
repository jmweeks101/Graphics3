from graphics import *
from base3D import *

def main():
    win = GraphWin("Graphics3",500,500)
    win.setCoords(0,0,10,10)
    testPrisim(win)
    win.close()

def testPrisim(win):
    cube = Prisim(win,Point(4,4),2,2,2)
    cube.show()
    win.getMouse()
    #fill color
    cube.fill("blue")
    win.getMouse()
    #move
    cube.translate(-1,1)
    win.getMouse()
    #make label
    cube.setLabel("Our cube","red",20,0,0)
    cube.drawLabel()
    win.getMouse()
    #customize edges
    cube.setEdgeColor("green")
    cube.setEdgeSize(3)
    win.getMouse()
    #clone
    cube2 = cube.clone()
    cube2.translate(4,2)
    cube2.show()
    win.getMouse()
    #zoom
    cube.zoom(2)
    cube.setLabel("Our cube","red",20,0,0)
    cube.drawLabel()
    win.getMouse()

def testPyramid(win):
    pyramid = Pyramid(win,Point(6,6),5,4,2)
    pyramid.show()
    win.getMouse()
    #fill color
    pyramid.fill("blue")
    win.getMouse()
    #move
    pyramid.translate(-1,1)
    win.getMouse()
    #make label
    pyramid.setLabel("Our Pyramid","red",20,0,2)
    pyramid.drawLabel()
    win.getMouse()
    #customize edges
    pyramid.setEdgeColor("red")
    pyramid.setEdgeSize(3)
    win.getMouse()
    #hide
    pyramid.hide()
    win.getMouse()


if __name__ == "__main__":
    main()
