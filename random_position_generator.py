from random import random

from position import Position


class RandomPositionGenerator:
    def __init__(self, random_number_generator, limit):
        self.limit = limit
        self.random_number_generator = random_number_generator

    def get_position(self):
        x = self.random_number_generator.randint(0, self.limit)
        y = self.random_number_generator.randint(0, self.limit)
        return Position(x, y)
