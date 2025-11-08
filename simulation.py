from player import *
from wall import *
from ray import *

class Simulation :
    def __init__(self):
        self.player = Player(500, 500, 0)
        self.walls = Walls()
        self.rays = self.__return_rays()
        self.first_wall_coordinate = False

    
    def __return_rays(self) -> list[Ray]:
        orientation = self.player.orientation
        rays = [ Ray(self.player.x, self.player.y, orientation, i/2) 
                for i in range(-45*2, 45*2) ]
        return rays


    def refresh_rays(self):
        self.rays = self.__return_rays()
        for ray in self.rays:
            ray.determine_intersection(self.walls.walls)


    def draw_debug_window(self):
        self.player.draw()
        for wall in self.walls.walls :
            wall.draw()
        for ray in self.rays:
            ray.draw()


    def draw_player_window(self):
        for ray in self.rays :
            ray.draw_player_window()