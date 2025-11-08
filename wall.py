import pyglet
from pyglet.math import Vec2

class Wall():
    def __init__(self, pos1 : Vec2, pos2 : Vec2):
        self.x1 = pos1.x
        self.y1 = pos1.y
        self.x2 = pos2.x
        self.y2 = pos2.y

    def draw(self) :
        pyglet.shapes.Line(self.x1, self.y1, self.x2, self.y2).draw()
        pyglet.shapes.Circle(self.x1, self.y1, 10).draw()
        pyglet.shapes.Circle(self.x2, self.y2, 10).draw()


class Walls():
    def __init__(self):
        self.walls : list[Wall] = []
        self.pending_coordiante = False

    #Return if rays must be refreshed
    def add_wall(self, mouse_x, mouse_y) -> True:

        new_pos = Vec2(mouse_x, mouse_y)

        if self.pending_coordiante == False:
            self.pending_coordiante = new_pos
            return False
        else:
            self.walls.append(Wall(new_pos, self.pending_coordiante))
            self.pending_coordiante = False
            return True