import pygame
import sys
from pygame.locals import *
from constants import *
from math import *


class Drag:
    """ Creates rectangular surfaces that can be dragged using mouse press """

    def __init__(self, rect):
        self.rect = rect
        self.pressed = False

    def drag(self, surface, image):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_dx, mouse_dy = pygame.mouse.get_rel()
        if pygame.mouse.get_pressed() == (1, 0, 0) and self.rect.collidepoint(mouse_x, mouse_y) and not self.pressed:
            self.pressed = True
        elif pygame.mouse.get_pressed() == (1, 0, 0) and self.pressed:
            self.rect.x += mouse_dx
            self.rect.y += mouse_dy
            surface.fill((0, 0, 0))
            surface.blit(image, self.rect.topleft)
        elif pygame.mouse.get_pressed() != (1, 0, 0):
            self.pressed = False



def main():
    clock = pygame.time.Clock()

    circle_x, circle_y = 20, 20
    pygame.draw.circle(root, RED, (circle_x, circle_y), 5)

    displacement = 0
    dx, dy = 0, 0

    speed = 100  # For small displacements the dx, dy become greater than the displacement so the point 'jumps'

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if pygame.mouse.get_pressed() == LEFT_PRESS and displacement == 0:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            displacement = int(sqrt((mouse_y - circle_y)**2+(mouse_x - circle_x)**2))
            direction = atan2(mouse_y - circle_y, mouse_x - circle_x)

            dx = cos(direction) * speed
            dy = sin(direction) * speed

            print(displacement)

        if displacement > 0:
            print(displacement)
            circle_x += dx
            circle_y += dy
            displacement -= speed
        else:
            displacement = 0

        x_new = int(circle_x)
        y_new = int(circle_y)

        pygame.draw.circle(root, RED, (x_new, y_new), 5)
        pygame.display.update()
        clock.tick(100)
        root.fill(BLACK)


if __name__ == '__main__':
    pygame.init()
    root = pygame.display.set_mode((1500, 1400))
    main()
