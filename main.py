import pygame
import sys
import random
from pygame.locals import *
from constants import *
from math import sin, cos, atan2, sqrt


class StoreBox:
    def __init__(self, x, y, order):
        self.occupied = True
        self.order = order,
        self.x, self.y = x, y

    def display(self, surface):
        surface.fill(RED, rect=(self.x, self.y, 100, 100))


class AnswerBox:
    def __init__(self, x, y, order):
        self.occupied = False
        self.order = order
        self.x, self.y = x, y

    def display(self, surface):
        surface.fill(RED, rect=(self.x, self.y, 100, 100))


class Letter:
    initial_layout = pygame.Surface(WINDOW_SIZE)
    for position in LETTERBOXES_POSITIONS:
        initial_layout.fill(GREEN, rect=(position[0], position[1], 100, 100))
        initial_layout.fill(RED, rect=(position[0], position[1] - LETTER_BUFF, 100, 100))

    def __init__(self, x, y, image, char):
        self.x = x
        self.y = y
        self.image = image
        self.char = char
        self.excited = False

    def excite(self, surface, speed=30):
        """ Moves a Letter to the leftmost available AnswerBox and leaves a StoreBox empty

            NB: In order for the letters to move fast and smoothly,
                a high FPS is needed (150) and 'speed' (25)

            For Future: See if the moving effect is good enough and whether you need to convert speed
                        into run_time or something like that """

        for answer_box in answer_boxes:
            if not answer_box.occupied:
                for store_box in store_boxes:
                    if store_box.x == self.x:
                        store_box.occupied = False
                        break
                answer_box.occupied = True
                self.excited = True
                target_x, target_y = answer_box.x, answer_box.y
                displacement = sqrt((target_x - self.x) ** 2 + (target_y - self.y) ** 2)
                direction = atan2(target_y - self.y, target_x - self.x)
                dx = cos(direction) * speed
                dy = sin(direction) * speed

                while displacement > 0:
                    check_termination()

                    if displacement <= int(sqrt(dx ** 2 + dy ** 2)) + speed:
                        self.x, self.y = target_x, target_y
                        displacement = 0
                    else:
                        self.x += dx
                        self.y += dy
                        displacement -= speed
                    x_new, y_new = int(self.x), int(self.y)
                    surface.blit(Letter.initial_layout, (0, 0))
                    for letter in letters:
                        surface.blit(letter.image, (letter.x, letter.y))
                    surface.blit(self.image, (x_new, y_new))
                    pygame.display.update()
                    clock.tick(150)
                break

    def de_excite(self, surface, speed=30):
        """ Moves a Letter from the rightmost occupied AnswerBox to the leftmost StoreBox """

        for store_box in store_boxes:
            if not store_box.occupied:
                for answer_box in answer_boxes:
                    if answer_box.x == self.x and answer_box.y == self.y:
                        answer_box.occupied = False
                        break
                store_box.occupied = True
                self.excited = False
                target_x, target_y = store_box.x, store_box.y
                displacement = sqrt((target_x - self.x) ** 2 + (target_y - self.y) ** 2)
                direction = atan2(target_y - self.y, target_x - self.x)
                dx = cos(direction) * speed
                dy = sin(direction) * speed

                while displacement > 0:
                    check_termination()

                    if displacement <= int(sqrt(dx ** 2 + dy ** 2)) + speed:
                        self.x, self.y = target_x, target_y
                        displacement = 0
                    else:
                        self.x += dx
                        self.y += dy
                        displacement -= speed
                    x_new, y_new = int(self.x), int(self.y)
                    surface.blit(Letter.initial_layout, (0, 0))
                    for letter in letters:
                        surface.blit(letter.image, (letter.x, letter.y))
                    surface.blit(self.image, (x_new, y_new))
                    pygame.display.update()
                    clock.tick(150)
                break

    def display(self, surface):
        surface.blit(self.image, (self.x, self.y))


def check_termination():
    if pygame.event.get(eventtype=QUIT):
        pygame.quit()
        sys.exit()


def check_excitation(keys_pressed_tpl):
    for i in range(97, 123):
        if keys_pressed_tpl[i]:
            pressed_letter = KEYS[i]
            for letter in letters:
                if letter.char == pressed_letter and not letter.excited:
                    letter.excite(root)
                    break
            break


def check_de_excitation(keys_pressed_tpl):
    if keys_pressed_tpl[K_BACKSPACE]:
        for answer_box in reversed(answer_boxes):
            if answer_box.occupied:
                for letter in letters:
                    if letter.x == answer_box.x and letter.y == answer_box.y:
                        letter.de_excite(root)
                        break
                break


def get_letter_actions():
    keys_pressed = pygame.key.get_pressed()
    check_excitation(keys_pressed)
    check_de_excitation(keys_pressed)


def main():
    order = 0
    for position in LETTERBOXES_POSITIONS:
        letter = random.choice(ALPHABET_LETTERS)
        letters.append(Letter(position[0], position[1], pygame.image.load(f'letters/{letter}.png'), letter))
        store_boxes.append(StoreBox(position[0], position[1], order))
        answer_boxes.append(AnswerBox(position[0], position[1] - LETTER_BUFF, order))
        order += 1
    else:
        del order, letter

    for order in range(9):
        letters[order].display(root)
        answer_boxes[order].display(root)

    while True:
        get_letter_actions()

        check_termination()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    letters = []
    answer_boxes = []
    store_boxes = []
    root = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    main()
