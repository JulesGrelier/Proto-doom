import random
import pyglet

from pyglet.window import key
from wall import *
from player import *

window = pyglet.window.Window(1080, 720, None)

player = Player(Vec2(500, 500), 0)

walls = [
    Wall(
        Vec2(random.randint(0, 1080), random.randint(0, 720)),
        Vec2(random.randint(0, 1080), random.randint(0, 720))
    ) 
    for i in range(1, 5)]

@window.event
def on_key_press(symbol, _):

    if symbol == key.LEFT:
        player.x -= 50
    if symbol == key.RIGHT:
        player.x += 50
    if symbol == key.DOWN:
        player.y -= 50
    if symbol == key.UP:
        player.y += 50

    if symbol == key.A:
        player.increase_orientation(-10)
    if symbol == key.Z:
        player.increase_orientation(10)


@window.event
def on_draw() :
    window.clear()

    for wall in walls :
        wall.draw()

    player.draw()

pyglet.app.run(1/30)