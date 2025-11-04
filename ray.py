from math import cos, sin, radians, sqrt
from wall import Wall

import pyglet
from pyglet.math import Vec2

class Ray():
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self.vector_x, self.vector_y = self.__return_coordinates_from_orientation(orientation)
        self.intersection = False

    def __return_coordinates_from_orientation(self, orientation):
        vector_x = cos(radians(orientation))
        vector_y = sin(radians(orientation))

        return vector_x, vector_y
    
    def draw(self):
        if self.intersection != False:
            pyglet.shapes.Line(self.x, self.y, self.intersection.x, self.intersection.y, color=(0, 0, 255)).draw()

    def draw_player_window(self):
        if self.intersection != False:
            pyglet.shapes.Circle(self.intersection.x, self.intersection.y, 10).draw()
    
    def __return_intersection(self, wall : Wall) -> Vec2:
        #Refers to https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
        x1 = wall.x1
        y1 = wall.y1
        x2 = wall.x2
        y2 = wall.y2

        x3 = self.x
        y3 = self.y
        x4 = self.x + self.vector_x
        y4 = self.y + self.vector_y

        #commun denominator of t and u, not Px and Py
        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denominator == 0:
            return False

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
        if t<0 or t>1:
            return False

        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator
        if u<0:
            return False
        
        Px = x1 + t*(x2-x1)
        Py = y1 + t*(y2 -y1)

        return Vec2(Px, Py)
        
    def __return_distance(self, P : Vec2):
        delta_x = P.x - self.x
        delta_y = P.y - self.y
        return sqrt(delta_x**2 + delta_y**2)
    
    def determine_intersection(self, walls : list[Wall]):

        for wall in walls:
            intersection = self.__return_intersection(wall)

            # if there isn't an intersection
            if intersection == False:
                #print("pas d'intersection")
                continue
            
            # if it's the first one to have an intersection
            elif self.intersection == False:
                print(type(intersection))
                print(f"nouvelle intersection faute de mieux qui est : {intersection.x}, {intersection.y}")
                self.intersection = intersection

            #If the precedent intersection is nearer
            elif self.__return_distance(self.intersection) < self.__return_distance(intersection):
                print("pas de meilleur intersection")
                continue
            
            #If there is a intersection nearar than the precedent one
            else:
                print(type(intersection))
                print(f"nouvelle intersection qui est : {intersection.x}, {intersection.y}")
                self.intersection = intersection