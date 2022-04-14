import sys
sys.path.insert(0, 'C:\\Users\\joshm\\OneDrive\\Documents\\Computer Science')
from graphics import *

import numpy as np

class Rhombus(GraphicsObject):
    #Uses the already existing polygon class to create a rhombus.
    #Gets a center point, length, and bottom left angle.
    def __init__(self, center, length, angle):
        #Bottom left point
        p1 = Point(center.getX() - (length/2), center.getY() - (length/2))
        #Bottom right point
        p2 = Point(center.getX() + (length/2), center.getY() - (length/2))
        #Top left point
        p3 = Point(p1.getX()+(length*np.cos(np.radians(angle))), p1.getY()+(length*np.sin(np.radians(angle))))
        #Top right point
        p4 = Point(p2.getX()+(length*np.cos(np.radians(angle))), p2.getY()+(length*np.sin(np.radians(angle))))
        self.points = [p1,p2,p4,p3]
        GraphicsObject.__init__(self, ["outline", "width", "fill"])

    def clone(self):
        other = Rhombus(*self.points)
        other.config = self.config.copy()
        return other

    def getPoints(self):
        return list(map(Point.clone, self.points))

    def _move(self, dx, dy):
        for p in self.points:
            p.move(dx,dy)

    def _draw(self, canvas, options):
        args = [canvas]
        for p in self.points:
            x,y = canvas.toScreen(p.x,p.y)
            args.append(x)
            args.append(y)
        args.append(options)
        return GraphWin.create_polygon(*args)


def main():
    win = GraphWin('GraphicsGroup', 600,600)
    win.setBackground('white')
    win.setCoords(0,0,10,10)

    test = Rhombus(Point(5,5), 2, 120)
    test.draw(win)
    test.setFill('black')

    win.getMouse()


if __name__ == '__main__':
    main()
