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
        #self.pos = (self.pos[0] + self.dir_x, self.pos[1] + self.dir_y)


    def draw(self, surface):
        dis = self.width // self.rows
        i = self.pos[0]
        j = self.pos[1]
        pygame.draw.rect(surface, self.colour, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))

    def return_pos(self):
        cube_x = self.pos[0]
        cube_y = self.pos[1]
        return cube_x, cube_y


class Snake(object):
    body = []
    turns = {}

    def __init__(self, pos, colour):
        self.colour = colour
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dir_x = 1
        self.dir_y = 0

    def move(self):
        tail = self.body[-1]

        #self.body.pop()
        #self.body.append(Cube((tail.pos[0] + self.dir_x, tail.pos[1] + self.dir_y), colour=GREEN))
        #self.body.append(Cube((tail.pos[0] + self.dir_x, tail.pos[1] + self.dir_y), colour=GREEN))
        #self.body.append(Cube((tail.pos[0] + self.dir_x, tail.pos[1] + self.dir_y), colour=GREEN))
        #self.body.append(Cube((tail.pos[0] + self.dir_x, tail.pos[1] + self.dir_y), colour=GREEN))
        self.body.append(Cube((tail.pos[0] + self.dir_x, tail.pos[1] + self.dir_y), colour=GREEN))
        self.body.append(Cube((tail.pos[0] + self.dir_x, tail.pos[1] + self.dir_y), colour=GREEN))
        #self.body.append(Cube((tail.pos[0] + self.dir_x, tail.pos[1] + self.dir_y), colour=GREEN))
        #self.body.append(Cube((tail.pos[0] + self.dir_x, tail.pos[1] + self.dir_y), colour=GREEN))
        #self.body.append(Cube((tail.pos[0] + self.dir_x, tail.pos[1] + self.dir_y), colour=GREEN))
        #self.body.append(Cube((tail.pos[0] + self.dir_x, tail.pos[1] + self.dir_y), colour=GREEN))
        #self.body.append(Cube((tail.pos[0] + self.dir_x, tail.pos[1] + self.dir_y), colour=GREEN))
        #self.body.append(Cube((tail.pos[0] + self.dir_x, tail.pos[1] + self.dir_y), colour=GREEN))
        #self.body.pop()

        for i, c in enumerate(self.body):
            #print(i, c.pos)
            self.body.append(Cube((tail.pos[0] + self.dir_x, tail.pos[1] + self.dir_y), colour=GREEN))
            self.body.pop(i)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        global left, right, up, down
        #print (left, right, up, down)
        print("Right is " + str(right))
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_LEFT] and right:
                print ("Applying left dir")
                self.dir_x = -1
                self.dir_y = 0
                left = False
                right = True
                down = True
                up = True
            elif keys[pygame.K_RIGHT] and left:
                self.dir_x = 1
                self.dir_y = 0
                right = False
                left = True
                down = True
                up = True
            elif keys[pygame.K_UP] and down:

                self.dir_x = 0
                self.dir_y = -1
                up = False
                down = True
                right = True
                left = True
            elif keys[pygame.K_DOWN] and up:
                self.dir_x = 0
                self.dir_y = 1
                down = False
                up = True
                right = True
                left = True
            # Prevent being able to go back on self


    def draw(self, surface):
        for i, c in enumerate(self.body):
            c.move(self.dir_x, self.dir_y)
            if i == 0:
                c.draw(surface)
            else:
                c.draw(surface)
            # Constrain it
            if i == 0:
                #print ("Snake Head is at " + str(c.pos[0]), str(c.pos[1]))
                if c.pos[0] > scale - 1:
                    c.pos = (0, c.pos[1])
                if c.pos[0] < 0:
                    c.pos = (scale - 1, c.pos[1])
                if c.pos[1] > scale - 1:
                    c.pos = (c.pos[0], 0)
                if c.pos[1] < 0:
                    c.pos = (c.pos[0], scale - 1)

    def addBlock(self):
        tail = self.body[-1]
        #self.body.append(Cube((tail.pos[0] - 1, tail.pos[1]), colour = GREEN))
        #self.body.append(Cube((tail.pos[0] + self.dir_x, tail.pos[1] + self.dir_y), colour=GREEN))


def random_food(row):
    # We're passed in the row the snakes head is on
    # This ensures the food can not be generated where the head is
    while True:
        f_row = random.randrange(scale)
        f_col = random.randrange(scale)
        if f_row == row:
            continue
        else:
            break
    return f_row, f_col


def main():

    loop = True
    global left, right, up, down
    left = False
    right = True
    up = True
    down = True
    pygame.init()
    pygame.display.set_caption("Snake V1.00")

    # Create our snake object
    s = Snake((10, 10), GREEN)
    # Create our initial food
    f = Cube(random_food(s.body[0].pos), colour=RED)
    while loop:
        # Update screen
        snake_surface.fill(BLACK)
        # Control FPS
        pygame.time.delay(80)
        clock.tick(30)
        # Move Snake
        s.move()
        pygame.display.update()


        # Draw Snake
        s.draw(snake_surface)

        # Draw Food
        f.draw(snake_surface)

        # Check collides
        if f.pos == s.body[0].pos:
            f = Cube(random_food(s.body[0].pos), colour=RED)
            s.addBlock()

        # Update the screen
        pygame.display.flip()


main()



