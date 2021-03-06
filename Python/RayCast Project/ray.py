import pygame
from numpy import array
from numpy import linalg
from numpy import cos, sin

class Ray:
    def __init__(self, x, y, radius):
        self.pos = [x, y]
        self.dir = array([cos(radius), sin(radius)])

    def display(self, screen):
        pygame.draw.line(screen, (255, 255, 255), self.pos, self.pos + self.dir, 1)
        
    def cast(self, wall):
        x1, y1 = wall.a[0], wall.a[1]
        x2, y2 = wall.b[0], wall.b[1]

        x3 = self.pos[0]
        y3 = self.pos[1]
        x4 = self.pos[0] + self.dir[0]
        y4 = self.pos[1] + self.dir[1]

        den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)
        num = (x1-x3) * (y3-y4) - (y1-y3) * (x3-x4)

        if den == 0:
            return None

        t = num/den
        u = -((x1-x2) * (y1-y3) - (y1-y2) * (x1-x3)) / den

        if t > 0 and t < 1 and u > 0:
            x = x1 + t * (x2-x1)
            y = y1 + t * (y2-y1)
            pot = array([x, y])
            return pot 
