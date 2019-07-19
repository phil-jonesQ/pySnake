import pygame
import random



# Global Variable
WindowWidth = 400
WindowHeight = 400
scale = 20
snake_pos_x = 3
snake_pos_y = 3
global my_dir
my_dir = 1

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


def draw_food():
    global food_pos_x, food_pos_y
    rect = pygame.Rect(food_pos_x * (scale + 1), food_pos_y * (scale + 1), scale, scale)
    pygame.draw.rect(snakewindow, RED, rect)


def draw_snake(direction):
    snake = ["1","2","3"]
    global snake_pos_x, snake_pos_y
    offset = scale + 1
    for blocks in snake:
        if direction == 1:
            offset += scale
            blocks = pygame.Rect(snake_pos_x * (scale + 1) + offset, snake_pos_y * (scale + 1), scale, scale)
        if direction == 0:
            offset -= scale
            blocks = pygame.Rect(snake_pos_x * (scale + 1) - offset, snake_pos_y * (scale + 1), scale, scale)
        if direction == 2:
            offset += scale
            blocks = pygame.Rect(snake_pos_x * (scale + 1), snake_pos_y * (scale + 1) + offset, scale, scale)
        if direction == -1:
            offset -= scale
            blocks = pygame.Rect(snake_pos_x * (scale + 1), snake_pos_y * (scale + 1) - offset, scale, scale)
        pygame.draw.rect(snakewindow, GREEN, blocks)


def move_snake(velocity, direction):
    #print("DEBUG: Velocity " + str(velocity) + " Direction " + str(direction) + " X = " + str(x) + " y = " + str(y))
    print (direction)
    global snake_pos_x, snake_pos_y
    if direction == 1:
        #print(x)
        snake_pos_x += velocity
    if direction == 0:
        snake_pos_x -= velocity
    if direction == 2:
        snake_pos_y += velocity
    if direction == -1:
        snake_pos_y -= velocity

    # Boundary rules
    if snake_pos_x > scale - 1:
        snake_pos_x = 0
    if snake_pos_x < 0:
        snake_pos_x = scale
    #print("Window Height = " + str(WindowHeight / scale) + "Snake POS = " + str(snake_pos_y))
    if snake_pos_y > scale:
        snake_pos_y = 0
    if snake_pos_y < 0:
        snake_pos_y = scale
    return

def scan_keys():
    global my_dir
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                my_dir = -1
            if event.key == pygame.K_DOWN:
                my_dir = 2
            if event.key == pygame.K_RIGHT:
                my_dir = 1
            if event.key == pygame.K_LEFT:
                my_dir = 0

def check_collision():
    global food_pos_x, food_pos_y
    if snake_pos_x == food_pos_x and snake_pos_y == food_pos_y:
        food_pos_x = random.randint(4, scale - 4)
        food_pos_y = random.randint(4, scale - 4)
        draw_food()



def main():

    # Variables
    loop = True
    global snake_pos_x, snake_pos_y, food_pos_x, food_pos_y
    snake_pos_x = 3
    snake_pos_y = 3
    food_pos_x = random.randint(4, scale - 4)
    food_pos_y = random.randint(4, scale - 4)
    wipe = pygame.color.Color('#FFFFFF')
    pygame.init()

    pygame.display.set_caption("Snake V1.00")
    while loop:
        snakewindow.fill(wipe)
        pygame.time.delay(150)
        clock.tick(40)
        pygame.display.update()
        #draw_grid()
        move_snake(1, my_dir)
        draw_snake(my_dir)
        draw_food()
        scan_keys()
        check_collision()


        # Update the screen
        pygame.display.flip()
        # Keep frame rate at 60 - clearly not needed for this type of game






# Call main
if __name__ == "__main__":
    main()
