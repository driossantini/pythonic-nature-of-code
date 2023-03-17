import pyglet
import numpy as np
from math import sqrt
from pyglet.math import Vec2


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
        self.pos = Vec2(self.x, self.y)
        self.velocity = Vec2(0,0)
        self.acceleration = Vec2(0,0)
        self.opacity = 200
        self.canvas_w, self.canvas_h = canvas_size

    def apply_force(self, force):
        """Apply a force to the mover. 

        Args:
            force (numpy.ndarray): A numpy array of the shape (2,)
                                   Example, numpy.array([1,1])
        """
        assert type(force) == Vec2, "The applied force has to be a 2D vector Vec2"
        f = force / self.mass
        self.acceleration = self.acceleration + f 

    def friction(self, mu):
        """Apply a friction force to the Mover
        """
        diff = self.pos.y - self.radius

        if diff < 1:
            # Direction of friction
            friction_f = Vec2(*self.velocity)
            friction_f = friction_f.normalize() * -1

            # Magnitude of friction
            normal = self.mass
            friction_f = friction_f.from_magnitude(mu*normal)
            self.apply_force(friction_f)

    def drag(self, c):
        """Apply a drag force to Mover
        """
        # Direction of drag
        drag_f = Vec2(*self.velocity)
        drag_f = drag_f.normalize() * -1

        # Magnitude of drag
        speed_sq = self.velocity.mag**2
        drag_f = drag_f.from_magnitude(c*speed_sq)

        self.apply_force(drag_f)

    def update(self, dt):
        """Updates the mover position on the canvas

        Args:
            dt (float): The number of seconds since the last “tick”.
                        Typically obtained from  pyglet.clock.schedule_interval()
        """

        self.velocity = self.velocity + self.acceleration  
        self.pos = self.pos + self.velocity * dt
        self.x = self.pos.x
        self.y = self.pos.y
        self.acceleration = Vec2(0,0)


    def check_edges(self):
        """Keeps the mover inside the canvas
        """
        # Checking position on canvas at the x axis
        if self.pos.x <= self.radius:
            self.pos.x = self.radius
            self.velocity.x *= -1
        elif self.pos.x >= self.canvas_w - self.radius:
            self.pos.x = self.canvas_w - self.radius
            self.velocity.x *= -1

        # Checking position at the y axis
        if self.pos.y <= self.radius:
            self.pos.y = self.radius
            self.velocity.y *= -1
        elif self.pos.y >= self.canvas_h - self.radius:
            self.pos.y = self.canvas_w - self.radius
            self.velocity.y *= -1
