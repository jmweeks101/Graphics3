from graphics import *

#Creates a sphere object
class Sphere:
    #Takes inputs of the center, radius, and height of sphere, as well as the rgb values (as a list) for the sphere
    #Side parameter determines which way the light is coming from, default is the right side.
    #Note: coordinates have to be set on graphics window for it to work properly.
    def __init__(self, center, radius, rgb, side='right'):
        self.side = side
        self.center = center
        self.radius = radius
        self.rgb = rgb

    #Creates the overall sphere as a circle
    def createCircle(self):
        circle = Circle(self.center, self.radius)
        circle.setFill(color_rgb(self.rgb[0],self.rgb[1],self.rgb[2]))
        circle.setOutline(color_rgb(self.rgb[0],self.rgb[1],self.rgb[2]))
        return circle

    #creates a smaller circle to apply a gradience, making it appear more 3D
    def createGradient(self):
        if self.side == 'right':
            gradient = Circle(Point(self.center.x+self.radius/4, self.center.y+self.radius/4), self.radius/1.6)
        else:
            gradient = Circle(Point(self.center.x-self.radius/4, self.center.y+self.radius/4), self.radius/1.6)
        gradient.setOutline(color_rgb(self.rgb[0],self.rgb[1],self.rgb[2]))
        self.gradientrgb = [self.rgb[0]+5,self.rgb[1]+5,self.rgb[2]+5]
        for i, color in enumerate(self.gradientrgb):
            if color>255:
                self.gradientrgb[i] = 255
        gradient.setFill(color_rgb(self.gradientrgb[0],self.gradientrgb[1],self.gradientrgb[2]))
        return gradient

    #Creates a highlight to make it appear even more 3D
    def createHighlight(self):
        if self.side == 'right':
            highlight = Oval(Point(self.center.x+self.radius/2.7, self.center.y+self.radius/1.6), Point(self.center.x+self.radius/2.0, self.center.y+self.radius/2.2))
        else:
            highlight = Oval(Point(self.center.x-self.radius/2.7, self.center.y+self.radius/1.6), Point(self.center.x-self.radius/2.0, self.center.y+self.radius/2.2))
        rgb = [self.rgb[0]+130,self.rgb[1]+130,self.rgb[2]+130]
        for i, color in enumerate(rgb):
            if color>255:
                rgb[i] = 0
        highlight.setFill(color_rgb(rgb[0], rgb[1], rgb[2]))
        highlight.setOutline(color_rgb(self.gradientrgb[0],self.gradientrgb[1],self.gradientrgb[2]))
        return highlight

    #Creates the shadow that the sphere would create.
    def createShadow(self):
        if self.side == 'right':
            shadow = Oval(Point(self.center.x+0.25*self.radius, self.center.y-self.radius/.9), Point(self.center.x-2*self.radius,self.center.y-self.radius/1.66))
        else:
            shadow = Oval(Point(self.center.x-0.25*self.radius, self.center.y-self.radius/.9), Point(self.center.x+2*self.radius,self.center.y-self.radius/1.66))
        shadow.setFill(color_rgb(30,30,30))
        return shadow

    #Takes the four objects and adds them in a list.
    def createSphere(self):
        sphere = [self.createShadow(), self.createCircle(), self.createGradient(), self.createHighlight()]
        return sphere



def main():
    win = GraphWin('', 500, 500)
    win.setCoords(0,0,10,10)
    sphere = Sphere(Point(5,5), 2, [100,100,100], side='left')
    for face in sphere.createSphere():
        face.draw(win)
    win.getMouse()

main()
