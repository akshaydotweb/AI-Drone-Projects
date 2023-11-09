import pygame

# initialize pygame
pygame.init()

# Create a pygame window
screen = pygame.display.set_mode((800, 600))

# get the size
x, y = screen.get_size()

pygame.quit()

print(x, y)