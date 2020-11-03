import pygame
import sys
import random
from pygame.locals import *
from constants import *
from math import sin, cos, atan2, sqrt


class LetterBox:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move_to(self, surface, target_pos, speed):
        displacement = int(sqrt((target_pos[1] - self.y)**2 + (target_pos[0] - self.x)**2))
        direction = atan2(target_pos[1] - self.y, target_pos[0] - self.x)

        dx = cos(direction) * speed
        dy = sin(direction) * speed

        while displacement > 0:
            surface.fill(BLACK, rect=((self.x, self.y), (100, 100)))
            if displacement < int(sqrt(dx**2 + dy**2)):
                self.x, self.y = target_pos
                displacement = 0
            else:
                self.x += dx
                self.y += dy
                displacement -= speed
            x_new, y_new = int(self.x), int(self.y)
            surface.blit(self.image, (x_new, y_new))
            pygame.display.update()
            clock.tick(FPS)


def main():
    pygame.init()

    root = pygame.display.set_mode(WINDOW_SIZE)

    img = pygame.image.load('letters/A.png')
    letter_a = LetterBox(20, 20, img)
    root.blit(img, (letter_a.x, letter_a.y))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if pygame.key.get_pressed()[K_a] == 1:
            letter_a.move_to(root, (200, 150), 8)
        elif pygame.key.get_pressed()[K_b] == 1:
            letter_a.move_to(root, (20, 20), 8)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    clock = pygame.time.Clock()
    main()
