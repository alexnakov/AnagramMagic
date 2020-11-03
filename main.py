import pygame
import sys
import random
from classes import *
from pygame.locals import *
from constants import *
from math import sin, cos, atan2, sqrt

class LetterBox:
    def __init__(self, rect):
        self.rect = rect  # pygame.Rect
        self.pressed = False

    def move_to(self, *args):
        displacement = int(sqrt(rect.x ))


    def mouse_drag(self, surface, image):
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
    pygame.init()

    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(WINDOW_CAPTION)

    letters = []
    letterboxes = []

    for i in range(9):
        letter = random.choice(ALL_ALPHABET_LETTERS)
        letters.append(Letter(letter, fr'letters/{letter}.png', [50 + 150*i, 650]))

        letterboxes.append(LetterBox([50 + 150*i, 400], i))

    for letter in letters:
        img = pygame.image.load(letter.path)
        window.blit(img, letter.position)

    for letterbox in letterboxes:
        rect = pygame.SurfaceType([letterbox.width, letterbox.height])
        rect.fill(RED)
        window.blit(rect, letterbox.position)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main()
