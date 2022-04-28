from graphics import *
from base3D import *

def main():
    win = GraphWin("Graphics3",500,500)
    win.setCoords(0,0,10,10)

    pyramid = Pyramid(win,Point(6,6),5,5,2)
    pyramid.show()
    pyramid.fill("blue")
    win.getMouse()
    pyramid.translate(-1,1)
    win.getMouse()
    pyramid.drawLabel("Our Pyramid","red",20)
    win.close()


if __name__ == "__main__":
    main()
