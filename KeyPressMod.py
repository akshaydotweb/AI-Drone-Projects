import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 300))

def getkey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyIn = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))

    if keyIn[myKey]:
        ans = True
    pygame.display.update()
    return ans


def main():
    if getkey("LEFT"):
        print("Left key pressed")

    if getkey("RIGHT"):
        print("Right key pressed")


if __name__ == "__main__":
    init()
    while True:
        main()