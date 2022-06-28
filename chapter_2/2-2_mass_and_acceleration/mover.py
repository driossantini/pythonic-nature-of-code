import pyglet
import numpy as np
from math import sqrt


class Mover(pyglet.shapes.Circle):
    """Creates a mover object with a basic circular shape

    Args:dx
        pyglet (): Inherits attributes from pyglet shapes.circle
    """

    def __init__(self, mass, *args, **kwargs, ):
        super().__init__(radius=sqrt(mass)*10, *args, **kwargs)

        self.mass = mass
        self.pos = np.array([float(self.x), float(self.y)])
        self.velocity = np.array([0., 0.])
        self.acceleration = np.array([0., 0.])

    def apply_force(self, force):
        """Apply a force to the mover. 

        Args:
            force (numpy.ndarray): A numpy array of the shape (2,)
                                   Example, numpy.array([1,1])
        """
        assert type(
            force) == np.ndarray, "The applied force has to be a numpy array"
        assert len(force.shape) == 1 and sum(
            force.shape) == 2, "The force has to be a 2D numpy array"
        f = force / self.mass
        self.acceleration += f

    def update(self, dt):
        """Updates the mover position on the canvas

        Args:
            dt (float): The number of seconds since the last “tick”.
                        Typically obtained from  pyglet.clock.schedule_interval()
        """

        self.acceleration *= dt
        self.velocity += self.acceleration
        self.pos += self.velocity
        self.x = self.pos[0]
        self.y = self.pos[1]

    def check_edges(self, canvas_w, canvas_h):
        """Keeps the mover inside the canvas

        Args:
            canvas_w (int): Width of the screen in pixels
            canvas_h (int): Height of the screen in pixels
        """
        # Checking position on canvas at the x axis
        if self.pos[0] <= self.radius:
            self.pos[0] = self.radius
            self.velocity[0] *= -1
        elif self.pos[0] >= canvas_w - self.radius:
            self.pos[0] = canvas_w - self.radius
            self.velocity[0] *= -1

        # Checking position at the y axis
        if self.pos[1] <= self.radius:
            self.pos[1] = self.radius
            self.velocity[1] *= -1
        elif self.pos[1] >= canvas_h - self.radius:
            self.pos[1] = canvas_h - self.radius
            self.velocity[1] *= -1
