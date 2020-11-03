import pygame
import sys
import random
from pygame.locals import *
from constants import *
from math import sin, cos, atan2, sqrt


class LetterBox:  # TODO ensure you can move letter boxes anywhere without deleting the screen
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.displacement = 0
        self.direction = 0
        self.dx, self.dy = 0, 0

    def move_to(self, surface, target_pos, speed=1):
        if not self.displacement:
            self.displacement = int(sqrt((target_pos[1] - self.y)**2 + (target_pos[0] - self.x)**2))
            self.direction = atan2(target_pos[1] - self.y, target_pos[0] - self.x)

            self.dx = cos(self.direction) * speed
            self.dy = sin(self.direction) * speed

        if (self.displacement > 0) and (self.displacement < int(sqrt(self.dx**2 + self.dy**2))):
            self.x, self.y = target_pos
            self.displacement = 0
        elif self.displacement > 0:
            print(self.displacement)
            self.x += self.dx
            self.y += self.dy
            self.displacement -= speed
        else:
            self.displacement = 0

        x_new = int(self.x)
        y_new = int(self.y)

        surface.fill(BLACK)
        surface.blit(self.image, (x_new, y_new))


def main():
    pygame.init()

    root = pygame.display.set_mode(WINDOW_SIZE)

    img = pygame.image.load('letters/A.png')
    letter_a = LetterBox(600, 400, img)
    root.blit(img, (letter_a.x, letter_a.y))

    root.blit(img, (0,500))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        letter_a.move_to(root, (0, 0), 10)
        root.blit(img, (0, 150))


        pygame.display.update()


if __name__ == '__main__':
    main()
