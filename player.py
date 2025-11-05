from math import radians, cos, sin

import pyglet
from pyglet.window import key


class Player() :
    def __init__(self, x, y, orientation : int):
        self.x = x
        self.y = y
        self.orientation = orientation #in degree



    def __increase_orientation(self, angle : int) :
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
    


    def deals_with_keyboard_inputs(self, symbol : key):
        orientation = False
        
        if symbol == key.LEFT:
            orientation = self.orientation + 90
        if symbol == key.RIGHT:
            orientation = self.orientation - 90
        if symbol == key.DOWN:
            orientation = self.orientation + 180
        if symbol == key.UP:
            orientation = self.orientation

        if orientation != False:
            self.x += cos(radians(orientation)) * 50
            self.y += sin(radians(orientation)) * 50

        if symbol == key.A:
            self.__increase_orientation(10)
        if symbol == key.Z:
            self.__increase_orientation(-10)