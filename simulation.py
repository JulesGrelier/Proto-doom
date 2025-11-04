from random import randint

from player import *
from wall import *
from ray import *

class Simulation :
    def __init__(self):
        self.player = self.__return_player()
        self.walls = self.__return_walls()
        self.rays = self.__return_rays()

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

        rays = [ Ray(self.player.x, self.player.y, i) 
                for i in range(orientation - 45, orientation + 45) ]
        
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
