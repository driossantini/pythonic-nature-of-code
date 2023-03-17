import pyglet
import numpy as np
from math import sqrt
from pyglet.math import Vec2


class Attractor(pyglet.shapes.Circle):
    def __init__(self, mass, *args, **kwargs):
        super().__init__(radius=sqrt(mass)*2, *args, **kwargs)
        
        self.mass = mass
        self.pos = Vec2(self.x,self.y)
        

    def attract(self, other):
        """Applies an attraction force to a mover object

        Args:
            other (Mover): Mover object to attract
        """
        force = self.pos - other.pos
        distance_sq = min(1000,max(100,force.mag**2))
        G = 5
        strength = G*(self.mass*other.mass)/distance_sq
        force = force.from_magnitude(strength)
        other.apply_force(force)
