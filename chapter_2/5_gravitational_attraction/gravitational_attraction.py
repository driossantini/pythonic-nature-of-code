import pyglet
from pyglet.window import mouse
from pyglet.math import Vec2
from mover import Mover
from attractor import Attractor
from random import randint

def mover_list(num, batch):
    """Create a list with num Mover(s) in random locations in the canvas

    Args:
        num (int): Number of movers to create
        batch (pyglet.graphics.Batch): Use batch method from Mover to draw all Movers in one batch

    Returns:
        list: List of (num) size of Movers
    """
    movers = []
    for _ in range(num):
        new_mover = Mover(x=randint(1, canvas.width), y=randint(1, canvas.height),
                          mass=randint(50, 150),
                          canvas_size=canvas.get_size(),
                          batch=batch)
        movers.append(new_mover)
    return movers

# Define window/canvas size
canvas = pyglet.window.Window(400, 400)

# Detect mouse events
mouse_buttons = mouse.MouseStateHandler()
canvas.push_handlers(mouse_buttons)

# Define drawing batch and sprites
main_batch = pyglet.graphics.Batch()
movers = mover_list(10, main_batch)
attractor = Attractor(mass=100, x=200, y=200, batch=main_batch, color=(255,0,100))

def canvas_update(dt):
    """Updates the canvas according to the frame rate dt.

    Args:
        dt (float): frame rate
    """
    for mover in movers:
        attractor.attract(mover)
        mover.update(dt)



@canvas.event
def on_draw():
    """Initialising canvas and drawing all sprites.
    """
    canvas.clear()
   
    # Note: Here, we are using the 'advanced' batch draw option
    # More info in https://pyglet.readthedocs.io/en/latest/modules/graphics/index.html
    main_batch.draw()


if __name__ == "__main__":
    pyglet.clock.schedule_interval(canvas_update, 1/240.0)
    pyglet.app.run()
