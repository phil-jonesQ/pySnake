import pygame
import random



# Global Variable
WindowWidth = 400
WindowHeight = 400
x_POS = WindowWidth / 2
y_POS = WindowHeight / 2
scale = 11

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (101, 152, 101)
GREY = (128, 128, 128)

snakewindow = pygame.display.set_mode((WindowWidth, WindowHeight))




# Use the pygame clock so we can set the frame rate of the game
clock = pygame.time.Clock()


def draw_grid():
    for y in range(WindowHeight):
        for x in range(WindowWidth):
            rect = pygame.Rect(x * (scale + 1), y * (scale + 1), scale, scale)
            pygame.draw.rect(snakewindow, RED, rect)


def draw_snake(x, y):
    snake = ["1"]
    snake_pos_x = x
    snake_pos_y = y
    for blocks in snake:
        rect = pygame.Rect(snake_pos_x * (scale + 1), snake_pos_y * (scale + 1), scale, scale)
        pygame.draw.rect(snakewindow, GREEN, rect)


def move_snake(velocity, direction, x, y):
    #print("DEBUG: Velocity " + str(velocity) + " Direction " + str(direction) + " X = " + str(x) + " y = " + str(y))
    if direction == 1:
        #print(x)
        x = x + velocity
        print(x)
    if direction == 0:
        x -= velocity
    if direction == -1:
        y += velocity
    if direction == 2:
        y -= velocity

    # Boundary rules
    if x > WindowWidth:
        x = 0

    return



def main():

    # Variables
    loop = True

    snake_pos_x = scale
    snake_pos_y = scale

    pygame.init()
    draw_grid()
    pygame.display.set_caption("Snake V1.00")
    while loop:

        move_snake(5, 1, snake_pos_x, snake_pos_y)

        draw_snake(snake_pos_x, snake_pos_y)

        snake_pos_x += 1

        #print(snake_pos_x)

        # Update the screen
        pygame.display.flip()

        # Keep frame rate at 60 - clearly not needed for this type of game
        clock.tick(10)
        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()




# Call main
if __name__ == "__main__":
    main()
