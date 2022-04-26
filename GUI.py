from graphics import *
from base3D import *

def main():
    win = GraphWin("Graphics3",500,500)
    win.setCoords(0,0,10,10)

    cube = Prisim(win,Point(6,6),1,4,2)
    cube.show()
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
