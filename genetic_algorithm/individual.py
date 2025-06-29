from random import random, randint
from math import sqrt

class CityOrder(object):
    
    # Each city has its number and x and y coordinates, while an individual is an ordered list of cities
    def __init__(self, order):
        self.order = order
        self.fitness = self.calc_fitness()

    def __str__(self): 
        return self.order
    
    def get_fitness(self):
        return self.fitness
    

    def calc_fitness(self):
        if len(self.order) == 0:
            self.fitness = -1
            return
        path_length = 0
        for i in range (1, len(self.order)):
            distance = sqrt((self.order[i-1][0] - self.order[i][0])**2 + (self.order[i-1][1] - self.order[i][1])**2)
            path_length += distance

        self.fitness = path_length

    def fill_path_random(self, data):

        city_order = []
        
        first_and_last_city = data[randint(0, len(data))-1]
        city_order.append(first_and_last_city)
        all_cities = [city for city in data]
        all_cities.remove(first_and_last_city)
        # data is a list of cities where one element (city) of a list is:
        # [index, x coord, y coord]
        # Iterating through list of cities while emptying at the same time
        while all_cities:

            current_index = randint(0, len(all_cities) -1)
            city_order.append(all_cities[current_index])
            all_cities.remove(all_cities[current_index])
        
        city_order.append(first_and_last_city)
        self.order = city_order
        self.calc_fitness()


    def mutate(self, chance):

        mutation_chance = random()

        if mutation_chance > chance:
            self.calc_fitness()
            return

        for city in self.order:
            pass

def cross_over(one_path, another_path):
    
    k1 = randint(0, len)