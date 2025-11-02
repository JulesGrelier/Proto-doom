from random import randint

from player import *
from wall import *


def return_player() -> Player:
    return Player(500, 500, 0)

def return_walls() -> list[Wall]:
    walls = [
    Wall(
        Vec2(randint(0, 1080), randint(0, 720)),
        Vec2(randint(0, 1080), randint(0, 720))
    ) 
    for i in range(1, 5)]

    return walls



class Simulation :
    def __init__(self):
        self.player = return_player()
        self.walls = return_walls()

    def draw(self):
        self.player.draw()

        for wall in self.walls :
            wall.draw()