import pyglet
from pyglet.window import mouse
import numpy as np
from mover import Mover

canvas = pyglet.window.Window(400, 400)

mover = Mover(x=200, y=200, radius=10,)

# Initialising mouse buttons and pushing them to the event stack.
# Similar to the following example:
# https://pyglet.readthedocs.io/en/latest/programming_guide/examplegame.html#giving-the-player-something-to-do
mouse_buttons = mouse.MouseStateHandler()
canvas.push_handlers(mouse_buttons)


def canvas_update(dt):
    """Updates the canvas according to the frame rate dt.

    Args:
        dt (_type_): frame rate
    """
    gravity = np.array([0, -10])
    mover.apply_force(gravity)

    # When left button of mouse is pressed apply wind force
    if mouse_buttons[mouse.LEFT]:
        wind = np.array([4, 0])
        mover.apply_force(wind)

    mover.check_edges()
    mover.update(dt)


@canvas.event
def on_draw():
    """Initialising canvas and drawing all sprites.
    """
    canvas.clear()
    mover.draw()


if __name__ == "__main__":
    pyglet.clock.schedule_interval(canvas_update, 1/240.0)
    pyglet.app.run()
