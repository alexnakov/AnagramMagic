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
        self.rect = Rect((self.x, self.y), (100, 100))
        self.pressed = False

    def move_to(self, surface, target_pos, speed):
        """ Moves a letterbox to specific coords with a specified speed """
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

    def drag(self, surface):
        """ When called, it allows for the user to drag the letter with their mouse """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_dx, mouse_dy = pygame.mouse.get_rel()

        if pygame.mouse.get_pressed() == LEFT_PRESS and self.rect.collidepoint(mouse_x, mouse_y) and not self.pressed:
            self.pressed = True
        elif pygame.mouse.get_pressed() == LEFT_PRESS and self.pressed:
            surface.fill(BLACK, rect=self.rect)
            self.rect.x += mouse_dx
            self.rect.y += mouse_dy
            self.x += mouse_dx
            self.y += mouse_dy
            surface.blit(self.image, (self.x, self.y))
        elif pygame.mouse.get_pressed() != LEFT_PRESS:
            self.pressed = False


def main():
    random_letter = random.choice(ALPHABET_LETTERS)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    root = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    main()
