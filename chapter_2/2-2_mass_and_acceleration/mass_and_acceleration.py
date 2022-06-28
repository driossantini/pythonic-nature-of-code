import pyglet
from pyglet.window import mouse
import numpy as np
from mover import Mover

canvas = pyglet.window.Window(400, 400)

mover_a = Mover(x=canvas.width//4, y=200, mass=2)
mover_b = Mover(x=canvas.width*3//4, y=200, mass=4)

# Initialising mouse buttons and pushing them to the event stack.
# Similar to the following example:
# https://pyglet.readthedocs.io/en/latest/programming_guide/examplegame.html#giving-the-player-something-to-do
mouse_buttons = mouse.MouseStateHandler()
canvas.push_handlers(mouse_buttons)


def canvas_update(dt):
    """Updates the canvas according to the frame rate dt.

    Args:
        dt (float): frame rate
    """
    gravity = np.array([0, -10])

    weigth_a = gravity * mover_a.mass
    weight_b = gravity * mover_b.mass

    mover_a.apply_force(weigth_a)
    mover_b.apply_force(weight_b)

    # Apply wind force when left button of mouse is pressed
    if mouse_buttons[mouse.LEFT]:
        wind = np.array([4, 0])
        mover_a.apply_force(wind)
        mover_b.apply_force(wind)

    mover_a.check_edges(*canvas.get_size())
    mover_a.update(dt)

    mover_b.check_edges(*canvas.get_size())
    mover_b.update(dt)


@canvas.event
def on_draw():
    """Initialising canvas and drawing all sprites.
    """
    canvas.clear()

    # Note: Pyglet has a more efficient function to draw multiple items on the screen
    # However, because we are in the first examples, I will not use it.
    mover_a.draw()
    mover_b.draw()


if __name__ == "__main__":
    pyglet.clock.schedule_interval(canvas_update, 1/240.0)
    pyglet.app.run()
