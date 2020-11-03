from constants import *


class Letter:
    def __init__(self, letter, path, position):
        self.path = path
        self.position = position
        self.letter = letter

    def __str__(self):
        return self.letter


class LetterBox:
    def __init__(self, position, number):
        self.position = position
        self.has_letter = False
        self.number = number  # Indicates which LetterBox it is from the left of the screen
        self.width = 100
        self.height = 100
        self.colour = RED


