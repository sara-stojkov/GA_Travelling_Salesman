from random import random, randint
from math import sqrt

class CityOrder(object):
    
    # Each city has its number and x and y coordinates, while an individual is an ordered list of cities
    def __init__(self, order):
        self.order = order
        self.fitness = self.get_fitness()

    def __str__(self):
        return self.order

    def get_fitness(self):
        path_length = 0
        for i in range (1, len(self.order)):
            distance = sqrt((self.order[i-1].x - self.order[i].x)**2 + (self.order[i-1].y - self.order[i].y)**2)
            path_length += distance

    def fill_path_random(self, data):
        pass

    def mutate(self, chance):

        mutation_chance = random()

        if mutation_chance > chance:
            self.fitness()
            return

        for city in self.order:
            pass