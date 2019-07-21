""" Version 1.00 - simple version of the snake game.. The game uses pygame to handle the graphics and is desinged on a
simple grid system (20,20 squares). This makes collision detection very easy. The algorithm I've used simply creates the
snake as a list of vectors and creates the movement by removing the last entry and appending a new offset entry (the
offset is dependent on the direction the snake is travelling in). The good thing about this algorithim is it doesn't need
any tracking of the snake direction and extra logic to handle how to append the snake.
Version 1.08 - Working game - need to add scoring and level up - i.e. speed up the game as the snake grows
Version 1.10 - Working game - Game over and levels added
Phil Jones July 2019 - phil.jones.24.4@gmail.com
"""

import pygame
import random

# Constants

WindowWidth = 520
WindowHeight = 600
scale = 25
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

    def draw(self, surface, head=False):
        dis = self.width // self.rows
        i = self.pos[0]
        j = self.pos[1]
        if head:
            pygame.draw.rect(surface, BLUE, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        else:
            pygame.draw.rect(surface, self.colour, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))


class Snake(object):
    body = []

    def __init__(self, pos, colour):
        self.colour = colour
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dir_x = 1
        self.dir_y = 0

    def move(self):
        tail = self.body[-1]
        global left, right, up, down, level, game_over

        if not game_over:
            # Append pop, append pop - shift register movement - always appending correct directions squares
            self.body.append(Cube((tail.pos[0] + self.dir_x, tail.pos[1] + self.dir_y), colour=GREEN))
            self.body.pop(0)

        if game_over:
            self.dir_x = 0
            self.dir_y = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_LEFT] and right and not game_over:
                self.dir_x = -1
                self.dir_y = 0
                left = False
                right = True
                down = True
                up = True
            elif keys[pygame.K_RIGHT] and left and not game_over:
                self.dir_x = 1
                self.dir_y = 0
                right = False
                left = True
                down = True
                up = True
            elif keys[pygame.K_UP] and down and not game_over:
                self.dir_x = 0
                self.dir_y = -1
                up = False
                down = True
                right = True
                left = True
            elif keys[pygame.K_DOWN] and up and not game_over:
                self.dir_x = 0
                self.dir_y = 1
                down = False
                up = True
                right = True
                left = True
            elif keys[pygame.K_SPACE] and game_over:
                self.reset((10, 10))

    def draw(self, surface):
        for i, c in enumerate(self.body):
            snakeLength = (len(self.body))
            head = snakeLength - 1
            if i == head:
                c.draw(surface, True)
            else:
                c.draw(surface)
            # Constrain it
            if i == head:
                if c.pos[0] > scale:
                    c.pos = (0, c.pos[1])
                if c.pos[0] < 0:
                    c.pos = (scale, c.pos[1])
                if c.pos[1] > scale:
                    c.pos = (c.pos[0], 0)
                if c.pos[1] < 0:
                    c.pos = (c.pos[0], scale)

    def add_block(self):
        tail = self.body[-1]
        self.body.insert(0,(Cube((tail.pos[0] + self.dir_x, tail.pos[1] + self.dir_y), colour=GREEN)))

    def reset(self, pos):
        # Snake property reset
        self.body = []
        self.head = Cube(pos)
        self.body.append(self.head)
        self.dir_x = 1
        self.dir_y = 0
        # Global property reset
        global left, right, up, down, level, frame_rate, game_over
        left = False
        right = True
        up = True
        down = True
        game_over = False
        level = 1
        frame_rate = 10


def random_food(row):
    # We've passed in the row the snakes head is on
    # This ensures the food can not be generated where the head is
    # To improve this we could ensure the food can't be generated on the snake
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
    # Declare Global Vars
    global left, right, up, down, level, frame_rate, game_over
    pygame.init()
    pygame.display.set_caption("Snake V1.10")

    # Initialise fonts we will use
    font = pygame.font.SysFont('Arial', 50, False, False)
    font2 = pygame.font.SysFont('Arial', 25, False, False)

    # Create our snake object
    s = Snake((10, 10), GREEN)
    # Create our initial food
    f = Cube(random_food(s.body[0].pos), colour=RED)
    # Rest/Initialise our snake and global vars
    s.reset((10, 10))
    while loop:

        # Update screen
        snake_surface.fill(BLACK)

        # Control FPS
        clock.tick(frame_rate)

        # Move Snake
        s.move()
        pygame.display.update()

        # Draw Snake
        s.draw(snake_surface)

        # Draw Food
        f.draw(snake_surface)

        # Check collides with food
        snakeLength = len(s.body)
        if f.pos == s.body[snakeLength - 1].pos:
            f = Cube(random_food(s.body[0].pos), colour=RED)
            s.add_block()

        # Check collides with self
        for each_block in range(snakeLength):
            if s.body[each_block].pos in list(map(lambda z: z.pos, s.body[each_block + 1:])):
                game_over = True
                break

        # Update Display for user
        text = font.render("SCORE " + str(snakeLength), True, WHITE)
        text2 = font.render("LEVEL " + str(level), True, WHITE)
        if game_over:
            text = font.render("SCORE " + str(snakeLength), True, WHITE)
            text2 = font.render("LEVEL " + str(level), True, WHITE)
            text_game_over = font2.render("GAME OVER!!! SPACE TO RESTART..", True, RED)
            snake_surface.blit(text_game_over, [80, WindowHeight - 400])
        pygame.draw.line(snake_surface, WHITE, (0, WindowHeight - 65), (WindowWidth, WindowHeight - 65))
        snake_surface.blit(text, [20, WindowHeight - 60])
        snake_surface.blit(text2, [WindowWidth - 190, WindowHeight - 60])

        # Update the screen
        pygame.display.flip()

        # Increase Level
        if snakeLength > 10:
            level = 2
        if snakeLength > 20:
            level = 3
        if snakeLength > 40:
            level = 4

        # Map level
        if level == 1:
            frame_rate = 10
        if level == 2:
            frame_rate = 12
        if level == 3:
            frame_rate = 16
        if level == 4:
            frame_rate = 20

# Call main
main()