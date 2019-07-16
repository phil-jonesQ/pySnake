import pygame
import random



# Global Variable
WindowWidth = 800
WindowHeight = 800
x_POS = WindowWidth / 2
y_POS = WindowHeight / 2
scale = 22

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



def main():

    # Variables
    loop = True

    pygame.init()

    draw_grid()
    while loop:

        pygame.display.set_caption("Snake V1.00")



        # Update the screen
        pygame.display.flip()

        # Keep frame rate at 60 - clearly not needed for this type of game
        clock.tick(60)
        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                pygame.quit()




# Call main
if __name__ == "__main__":
    main()
