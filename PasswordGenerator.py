import random


class PasswordGenerator:
    NUMERIC = 1
    ALPHABET_UPPER = 2
    ALPHABET_LOWER = 4
    SPECIAL_CHAR = 8

    __word = [
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],

        ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z"],

        ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"],

        ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@",
         "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"],
    ]

    def __init__(self, flag):
        self.symbol = []
        for i in range(4):
            if flag & (2 ** i) != 0:
                self.symbol += self.__word[i]

    def generate(self, digit):
        pwd = ""
        for i in range(digit):
            pwd += self.symbol[random.randint(0, len(self.symbol) - 1)]
        return pwd
