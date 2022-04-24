from graphics import *
import numpy as np

class Parallelogram(GraphicsObject):
    #Uses the already existing polygon class to create a rhombus.
    #Gets a center point, length, and bottom left angle.
    def __init__(self, center, length, width, angle):
        #Bottom left point
        self.p1 = Point(center.getX() - (width/2), center.getY() - (length/2))
        #Bottom right point
        self.p2 = Point(center.getX() + (width/2), center.getY() - (length/2))
        #Top left point
        self.p3 = Point(self.p1.getX()+(length*np.cos(np.radians(angle))), self.p1.getY()+(length*np.sin(np.radians(angle))))
        #Top right point
        self.p4 = Point(self.p2.getX()+(length*np.cos(np.radians(angle))), self.p2.getY()+(length*np.sin(np.radians(angle))))
        self.points = [self.p1,self.p2,self.p4,self.p3]
        GraphicsObject.__init__(self, ["outline", "width", "fill"])

    def clone(self):
        other = Parallelogram(*self.points)
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

    def create3(self):
        frontface = Parallelogram(Point(5,5), l, w, 90)
        topface = Parallelogram(Point(test.p3.x+(w/2), test.p3.y+(np.sin(np.radians(27.5))*l/2)), np.sin(np.radians(27.5))*l, w, 45)
        sideface = Polygon(test.p2, Point(test2.p4.x, test.p2.y+test2.p4.y-test.p4.y), test2.p4, test.p4)
        return [frontface, topface, sideface]


def main():
    win = GraphWin('GraphicsGroup', 600,600)
    win.setBackground('white')
    win.setCoords(0,0,10,10)

    test = Parallelogram(Point(3,5), 2, 4, 90)
    test.draw(win)
    test.setFill('black')

    win.getMouse()


if __name__ == '__main__':
    main()
