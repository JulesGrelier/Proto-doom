from random import randint

from player import *
from wall import *
from ray import *

class Simulation :
    def __init__(self):
        self.player = self.__return_player()
        self.walls = self.__return_walls()
        self.rays = self.__return_rays()
        self.first_wall_coordinate = False

    def __return_player(self) -> Player:
        return Player(500, 500, 0)

    def __return_walls(self) -> list[Wall]:
        walls = [
        Wall(
            Vec2(randint(0, 1080), randint(0, 720)),
            Vec2(randint(0, 1080), randint(0, 720))
        ) 
        for i in range(0, 5)]
        return walls
    


    def __return_rays(self) -> list[Ray]:
        orientation = self.player.orientation

        rays = [ Ray(self.player.x, self.player.y, orientation, i/2) 
                for i in range(-45*2, 45*2) ]
        
        return rays



    def refresh_rays(self):
        self.rays = self.__return_rays()

        for ray in self.rays:
            ray.determine_intersection(self.walls)



    def draw_debug_window(self):
        self.player.draw()

        for wall in self.walls :
            wall.draw()

        for ray in self.rays:
            ray.draw()



    def draw_player_window(self):
        for ray in self.rays :
            ray.draw_player_window()


    def add_wall(self, x, y):
        if self.first_wall_coordinate == False:
            self.first_wall_coordinate = Vec2(x, y)
        else:
            self.walls.append(Wall(self.first_wall_coordinate, Vec2(x, y)))
            self.first_wall_coordinate = False
