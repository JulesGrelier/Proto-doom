import pyglet
from pyglet.math import Vec2

from math import radians, cos, sin

BLUE = [0, 0, 255]

class Player() :
    def __init__(self, pos : Vec2, orientation : int):
        self.x = pos.x
        self.y = pos.y
        self.orientation = orientation #in degree

    def increase_orientation(self, angle : int) :
        print(f"Angle : {self.orientation} -> {self.orientation + angle}")
        self.orientation += angle

    def draw(self):
        pyglet.shapes.Circle(self.x, self.y, 10, ).draw()
        self.__draw_view()


    def __draw_view(self) :
        projection_left_x = cos(radians(self.orientation-45)) * 100
        projection_left_y = sin(radians(self.orientation-45)) * 100

        projection_right_x = cos(radians(self.orientation+45)) * 100
        projection_right_y = sin(radians(self.orientation+45)) * 100
        
        pyglet.shapes.Line(self.x, self.y, self.x + projection_left_x, self. y + projection_left_y).draw()
        pyglet.shapes.Line(self.x, self.y, self.x + projection_right_x, self. y + projection_right_y).draw()
    
