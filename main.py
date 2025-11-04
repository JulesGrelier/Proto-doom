import pyglet
from simulation import Simulation

debug_window = pyglet.window.Window(1080, 720, "Debug window", None)
player_window = pyglet.window.Window(1080, 720, "Player window", None)
simulation = Simulation()

@debug_window.event
def on_key_press(symbol, _):
    simulation.player.deals_with_keyboard_inputs(symbol)
    simulation.refresh_rays()

@debug_window.event
def on_draw() :
    debug_window.clear()
    simulation.draw_debug_window()

@player_window.event
def on_draw():
    debug_window.clear()
    simulation.draw_player_window()

pyglet.app.run(1/30)