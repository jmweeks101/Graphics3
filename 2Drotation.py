#Function designed to be able to rotate shapes on the 2D plane. This will
#allow us to manipulate the shapes in order to make them appear 3D.
import numpy as np

def rotate(shape, degrees):
    origin = shape.getCenter
    p1 = np.matrix([[shape.p1.x], [shape.p1.y]])
    p2 = np.matrix([[shape.p2.x], [shape.p2.y]])
    matrix = np.matrix([[np.cos(degrees), -np.sin(degrees)], [np.sin(degrees), np.cos(degrees)]])
    newp1x, newp1y = np.multiply(p1, matrix)
    newp2x, newp2y = np.multiply(p2, matrix)
