import pyglet
import numpy as np
from math import sqrt


def normalise_vector(vector):
    """Normalises a vector

    Args:
        vector (numpy.ndarray): A numpy vector
    """
    return vector/np.linalg.norm(vector)


def set_magnitude(vector, mag):
    """Sets the magnitude of a vector to mag

    Args:
        vector (numpy.ndarray): The numpy vector
        mag (float): Desired magnitude
    """

    return mag * normalise_vector(vector)


class Mover(pyglet.shapes.Circle):
    """Creates a mover object with a basic circular shape

    Args:
        pyglet (): Inherits attributes from pyglet shapes.circle
        canvas_size (tuple): Width and height of the screen in pixels
        mass (float): Mass of the mover 
    """

    def __init__(self, mass, canvas_size, *args, **kwargs, ):
        super().__init__(radius=sqrt(mass)*10, *args, **kwargs)

        self.mass = mass
        self.pos = np.array([float(self.x), float(self.y)])
        self.velocity = np.array([0., 0.])
        self.acceleration = np.array([0., 0.])
        self.opacity = 200
        self.canvas_w, self.canvas_h = canvas_size

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

    def friction(self):
        """Apply a friction force to the Mover
        """
        diff = self.pos[1] - self.radius
        if diff < 1 and np.any(self.velocity):
            # print('Friction')

            # Direction of friction
            friction = np.copy(self.velocity)
            friction = -1 * normalise_vector(friction)

            # Magnitude of friction
            mu = 0.2
            normal = self.mass
            friction = set_magnitude(vector=friction, mag=mu*normal)
            self.apply_force(friction)

    def update(self, dt):
        """Updates the mover position on the canvas

        Args:
            dt (float): The number of seconds since the last “tick”.
                        Typically obtained from  pyglet.clock.schedule_interval()
        """

        self.velocity += self.acceleration
        self.pos += self.velocity * dt
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.acceleration = np.array([0., 0.])

    def check_edges(self):
        """Keeps the mover inside the canvas
        """
        # Checking position on canvas at the x axis
        if self.pos[0] <= self.radius:
            self.pos[0] = self.radius
            self.velocity[0] *= -1
        elif self.pos[0] >= self.canvas_w - self.radius:
            self.pos[0] = self.canvas_w - self.radius
            self.velocity[0] *= -1

        # Checking position at the y axis
        if self.pos[1] <= self.radius:
            self.pos[1] = self.radius
            self.velocity[1] *= -1
        elif self.pos[1] >= self.canvas_h - self.radius:
            self.pos[1] = self.canvas_w - self.radius
            self.velocity[1] *= -1
