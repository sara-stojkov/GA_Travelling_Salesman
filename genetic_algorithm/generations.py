# This module will contain all data concerning the Genetic Algorithm - defining the initial generation, fitness function,
# and mutations

from const import POPULATION_SIZE

class individual(object):
    
    # Each city has its number and x and y coordinates, while an individual is an ordered list of cities
    def __init__(self, order):
        self.order = order

    def fitness(self):

        for city in self.cities:
            pass