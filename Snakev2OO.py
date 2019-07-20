import pygame
import random

# Constants

WindowWidth = 500
WindowHeight = 500
scale = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (101, 152, 101)
GREY = (128, 128, 128)
snake_surface = pygame.display.set_mode((WindowWidth, WindowHeight))
clock = pygame.time.Clock()


class Cube(object):
    rows = scale
    width = 500

    def __init__(self, start, dir_x=1, dir_y=0, colour=GREEN):
        self.pos = start
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.colour = colour

    def move(self, dir_x, dir_y):
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.pos = (self.pos[0] + self.dir_x, self.pos[1] + self.dir_y)

    def draw(self, surface):
        dis = self.width // self.rows
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(snake_surface, self.colour, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))


class Snake(object):
    body = []
    turns = {}

    def __init__(self, pos, colour):
        self.colour = colour
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dir_x = 0
        self.dir_y = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface)
            else:
                c.draw(surface)




def main():

    loop = True

    pygame.init()
    pygame.display.set_caption("Snake V1.00")

    # Create our snake object

    s = Snake((10, 10), GREEN)
    while loop:
        # Update screen
        snake_surface.fill(BLACK)
        pygame.time.delay(150)
        clock.tick(40)
        pygame.display.update()

        # Move Snake
        s.move()
        # Draw Snake
        s.draw(snake_surface)
        # Update the screen
        pygame.display.flip()


main()



