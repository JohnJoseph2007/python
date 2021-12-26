import pygame
import numpy
from limits import *
from particle import *

WIDTH = 800
HEIGHT = 800
SCREEN = (WIDTH, HEIGHT)

class Display:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN)

        pygame.display.set_caption("RayCast")

        self.walls = []
        for i in range(5):

            x1 = numpy.random.randint(0, WIDTH)
            y1 = numpy.random.randint(0, HEIGHT)

            x2 = numpy.random.randint(0, WIDTH)
            y2 = numpy.random.randint(0, HEIGHT)

            x3 = numpy.random.randint(0, WIDTH)
            y3 = numpy.random.randint(0, HEIGHT)

            self.walls.append(limits(x1, y1, x2, y2))
        self.walls.append(limits(0, 0, WIDTH, 0))
        self.walls.append(limits(0, 0, 0, HEIGHT))
        self.walls.append(limits(0, HEIGHT, WIDTH, HEIGHT))
        self.walls.append(limits(WIDTH, 0, WIDTH, HEIGHT))
        self.particle = Particle()
        
        self.stop = False
        self.clock = pygame.time.Clock()

    def Draw(self):
        for wall in self.walls:
            wall.display(self.screen)
        self.particle.display(self.screen)

    def run(self):
        while not self.stop:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop = True

                if event.type == pygame.MOUSEMOTION:
                    pos = event.pos
                    self.particle.pos[0] = pos[0]
                    self.particle.pos[1] = pos[1]

            self.particle.look(self.screen, self.walls)
            self.Draw()
            self.clock.tick(100)
            pygame.display.update()

if __name__ == '__main__':
    a = Display()
    a.run()
