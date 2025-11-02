import pyglet
from simulation import Simulation

window = pyglet.window.Window(1080, 720, None)
simulation = Simulation()

@window.event
def on_key_press(symbol, _):
    simulation.player.deals_with_keyboard_inputs(symbol)

@window.event
def on_draw() :
    window.clear()
    simulation.draw()

pyglet.app.run(1/30)