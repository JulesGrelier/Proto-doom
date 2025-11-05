from math import cos, sin, radians, hypot, pi, atan

from wall import Wall

import pyglet
from pyglet.math import Vec2


class Intersection():
    def __init__(self, x, y, distance_from_player):
        self.x = x
        self.y = y
        self.distance = distance_from_player


class Ray():
    def __init__(self, x, y, player_orientation, padding):
        self.relative_orientation_for_player = padding + 45
        self.Ax, self.Ay = x, y
        self.Bx, self.By = self.__return_B_from_orientation(player_orientation + padding)
        self.intersection = False

    def __return_B_from_orientation(self, orientation):
        vector_x = cos(radians(orientation))
        vector_y = sin(radians(orientation))

        Bx = self.Ax + vector_x
        By = self.Ay + vector_y

        return Bx, By
    

    
    def draw(self):
        if self.intersection != False:
            pyglet.shapes.Line(self.Ax, self.Ay, self.intersection.x, self.intersection.y, color=(0, 0, 255)).draw()



    def draw_player_window(self):
        if self.intersection == False:
            return
        
        width = 720/90
        x = 1080 - radians(self.relative_orientation_for_player) * 2160 / pi - width

        fixed_distance = self.intersection.distance * cos(radians(self.relative_orientation_for_player - 45))
        height = atan(200/fixed_distance) * 1440 / pi 

        y = 360 - height/2

        brightness = max(255 - int(self.intersection.distance/2), 0)
        color = (brightness, brightness, brightness)

        pyglet.shapes.Rectangle(x, y, width, height, color).draw()
    


    def __return_intersection(self, wall : Wall) -> Vec2:
        #Refers to https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
        x1 = wall.x1
        y1 = wall.y1
        x2 = wall.x2
        y2 = wall.y2

        x3 = self.Ax
        y3 = self.Ay
        x4 = self.Bx
        y4 = self.By

        #commun denominator of t and u, not Px and Py
        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denominator == 0:
            return False

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
        if t<=0 or t>=1:
            return False

        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator
        if u<0:
            return False
        
        Px = x1 + t*(x2-x1)
        Py = y1 + t*(y2 -y1)

        return Vec2(Px, Py)
    


    def determine_intersection(self, walls : list[Wall]):

        for wall in walls:
            intersection = self.__return_intersection(wall)

            # if there isn't an intersection
            if intersection == False:
                continue

            #There is a intersection, calcul of distance
            distance = hypot(self.Ax - intersection.x, self.Ay - intersection.y)
            
            # if it's the first one to have an intersection
            if self.intersection == False:
                self.intersection = Intersection(intersection.x, intersection.y, distance)
                continue

            #If the precedent intersection is nearer
            if self.intersection.distance < distance:
                continue
            
            #If there is a intersection nearar than the precedent one
            else:
                self.intersection = Intersection(intersection.x, intersection.y, distance)
                continue