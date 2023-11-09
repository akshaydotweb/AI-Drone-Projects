import pygame

pygame.init()

# creating a window
my_win = pygame.display.set_mode((480, 300))

color = (255, 0, 0)

pygame.draw.rect(my_win, color, pygame.Rect(30, 30, 60, 60))
pygame.display.flip()