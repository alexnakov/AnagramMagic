import pygame
import sys
import random
from pygame.locals import *
from constants import *
from math import sin, cos, atan2, sqrt


class AnswerBox:
    def __init__(self, x, y, order):
        self.occupied = False
        self.order = order
        self.x, self.y = x, y

    def display(self, surface):
        surface.fill(RED, rect=(self.x, self.y, 100, 100))


class Letter:
    def __init__(self, x, y, image, letter):
        self.x = x
        self.y = y
        self.image = image
        self.rect = Rect((self.x, self.y), (100, 100))
        self.pressed = False
        self.letter = letter

    def move_to(self, surface, target_pos, speed):
        """ Moves a letterbox to specific coords with a specified speed """
        displacement = int(sqrt((target_pos[1] - self.y)**2 + (target_pos[0] - self.x)**2))
        direction = atan2(target_pos[1] - self.y, target_pos[0] - self.x)
        dx = cos(direction) * speed
        dy = sin(direction) * speed

        while displacement > 0:
            surface.fill(BLACK, rect=((self.x, self.y), (100, 100)))

            if displacement <= int(sqrt(dx**2 + dy**2)) + speed:
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
            self.display(surface)
        elif pygame.mouse.get_pressed() != LEFT_PRESS:
            self.pressed = False

    def display(self, surface):
        surface.blit(self.image, (self.x, self.y))


def main():

    letters = {}
    answer_boxes = {}

    order = 0
    for position in LETTERBOXES_POSITIONS:
        letter = random.choice(ALPHABET_LETTERS)
        letters[order] = Letter(position[0], position[1], pygame.image.load(f'letters/{letter}.png'), letter)
        answer_boxes[order] = AnswerBox(position[0], position[1] - LETTER_ANSWERBOX_BUFF, order)
        order += 1
    else:
        del order

    for order in range(9):
        letters[order].display(root)
        answer_boxes[order].display(root)

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
