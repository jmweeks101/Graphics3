from graphics import *

#Creates a sphere object
class Sphere:
    #Takes inputs of the center, radius, and height of sphere, as well as the rgb values for the sphere
    def __init__(self, win, center, radius, rgb):
        self.win = win
        self.center = center
        self.radius = radius
        self.rgb = rgb


    def createCircle(self):
        circle = Circle(self.center, self.radius)
        circle.setFill(color_rgb(self.rgb[0],self.rgb[1],self.rgb[2]))
        circle.setOutline(color_rgb(self.rgb[0],self.rgb[1],self.rgb[2]))
        return circle

    def createGradient(self):
        gradient = Circle(Point(self.center.x+self.radius/4, self.center.y-self.radius/4), self.radius/1.6)
        gradient.setOutline(color_rgb(self.rgb[0],self.rgb[1],self.rgb[2]))
        self.gradientrgb = [self.rgb[0]+5,self.rgb[1]+5,self.rgb[2]+5]
        for i, color in enumerate(self.gradientrgb):
            if color>255:
                self.gradientrgb[i] = 255
        gradient.setFill(color_rgb(self.gradientrgb[0],self.gradientrgb[1],self.gradientrgb[2]))
        return gradient

    def createHighlight(self):
        highlight = Oval(Point(self.center.x+self.radius/2.7, self.center.y-self.radius/1.6), Point(self.center.x+self.radius/2.0, self.center.y-self.radius/2.2))
        rgb = [self.rgb[0]+130,self.rgb[1]+130,self.rgb[2]+130]
        for i, color in enumerate(rgb):
            if color>255:
                rgb[i] = 0
        highlight.setFill(color_rgb(rgb[0], rgb[1], rgb[2]))
        highlight.setOutline(color_rgb(self.gradientrgb[0],self.gradientrgb[1],self.gradientrgb[2]))
        return highlight

    def createShadow(self):
        shadow = Oval(Point(self.center.x+0.25*self.radius, self.center.y+self.radius/.9), Point(self.center.x-2*self.radius,self.center.y+self.radius/1.66))
        # rgb = [self.rgb[0]-60,self.rgb[1]-60,self.rgb[2]-60]
        # for i, color in enumerate(rgb):
        #     if color<0:
        #         rgb[i] = 0
        shadow.setFill(color_rgb(30,30,30))
        return shadow

    def drawSphere(self):
        shadow = self.createShadow()
        shadow.draw(self.win)
        circle = self.createCircle()
        circle.draw(self.win)
        gradient = self.createGradient()
        gradient.draw(self.win)
        highlight = self.createHighlight()
        highlight.draw(self.win)


def main():
    win = GraphWin('', 500, 500)

    sphere = Sphere(win, Point(400, 250), 100,[100,100,100])
    sphere.drawSphere()
    win.getMouse()

main()
