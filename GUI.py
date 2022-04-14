from graphics import *
from base3D import *
from rhombus import Rhombus
from rotation2D import *

def main():
    win = GraphWin("Graphics3",500,500)
    win.setCoords(0,0,10,10)
    win.getMouse()

    test = Rhombus(Point(5,5), 2, 120)
    test.draw(win)
    win.getMouse()

    rotate(test,30)
    win.getMouse()
    
    win.close()


if __name__ == "__main__":
    main()
