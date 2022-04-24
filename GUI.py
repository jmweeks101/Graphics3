from graphics import *
from base3D import *

def main():
    win = GraphWin("Graphics3",500,500)
    win.setCoords(0,0,10,10)
    win.getMouse()

    cube = Prisim(win,Point(3,3),2,2,2)
    cube.show()


if __name__ == "__main__":
    main()
