# Name: Shimey Loo
# Date: 08/11/21
# Description: Programming Project 4 - Hangman Game

from random import *


def generate_word():
    """Returns a random word"""
    word_list = ("abruptly", "abyss",  "askew", "awkward", "bandwagon", "beekeeper", "blizzard", "bookworm", "buffalo",
                 "buzzard", "croquet", "cycle", "daiquiri", "dizzying", "embezzle", "espionage", "fishhook", "fixable",
                 "flapjack", "fluffiness", "funny", "galaxy", "gossip", "icebox", "jackpot", "jigsaw", "jogging",
                 "joyful", "jumbo", "lucky", "luxury", "microwave", "nightclub", "peekaboo", "puppy", "quizzes",
                 "strength", "unknown", "voodoo", "walkway", "waltz", "whiskey", "wimpy", "wizard", "youthful", "yummy",
                 "zigzag", "zipper", "zodiac", "zombie")
    random_number = randrange(50)
    random_word = word_list[random_number]
    return random_word


class Hangman:
    """ Class of a Hangman Game """

    def __init__(self):
        """ Initiates a game of Hangman """
        self.word = generate_word()
        self.guess = []
        for letter in self.word:
            self.guess.append("_")
        self.lives = 5

    def get_word(self):
        """ Getter for the word the client needs to guess """
        return self.word

    def get_guess(self):
        """ Getter for guesses the player has made """
        return self.guess

    def get_lives(self):
        """ Getter for lives remaining """
        return self.lives

    def set_guess(self):
        """ Setter for guess """

    def decrease_life(self):
        """ Decreases life by 1 """
        self.lives -= 1

    def submit_guess(self, letter):
        """
        Determines if given letter is in word.
            If letter is in work, self.guess will be updated to reflect that.
            If letter is not in work, lose a life.
        """
        count_letter_found = 0
        pos = 0
        for each_letter in self.word:            # Give letter was in word, update guess
            if letter == each_letter:
                count_letter_found += 1
                self.guess[pos] = letter
            pos += 1

        if count_letter_found == 0:              # Given letter was not in word, lose a life
            self.decrease_life()

