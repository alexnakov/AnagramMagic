import pygame
import sys
import random
from classes import *
from pygame.locals import *
from constants import *
from math import sin, cos, atan2, sqrt


class LetterBox:  # TODO ensure you can move letter boxes anywhere without deleting the screen
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move_to(self, surface, target_pos, speed):
        displacement = int(sqrt((target_pos[1] - self.y)**2 + (target_pos[0] - self.x)**2))
        direction = atan2(target_pos[1] - self.y, target_pos[0] - self.x)

        dx = cos(direction) * speed
        dy = sin(direction) * speed

        if displacement > 0:
            self.x += dx
            self.y += dy
            displacement += speed
        else:
            displacement = 0

        x_new = int(self.x)
        y_new = int(self.y)

        surface.fill(BLACK)
        surface.blit(self.image, (x_new, y_new))


def main():
    pygame.init()

    root = pygame.display.set_mode(WINDOW_SIZE)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main()
