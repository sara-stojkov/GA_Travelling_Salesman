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
            distance = sqrt((self.order[i-1].x - self.order[i].x)**2 + (self.order[i-1].y - self.order[i].y)**2)
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
        """
        Mutates the path by swapping n cities with a given chance.
        The number of cities to swap is determined randomly, but is between 2 and half of all the cities."""

        mutation_chance = random()

        if mutation_chance > chance:
            self.calc_fitness()
            return
        
        num_cities_to_swap = randint(2, len(self.order) // 2)
        # Randomly select cities to swap
        indices_to_swap = set()     
        while len(indices_to_swap) < num_cities_to_swap:
            indices_to_swap.add(randint(0, len(self.order) - 1))
        indices_to_swap = list(indices_to_swap)
        # Swap the selected cities
        for i in range(len(indices_to_swap) // 2):  
            index1 = indices_to_swap[i]
            index2 = indices_to_swap[len(indices_to_swap) - 1 - i]
            self.order[index1], self.order[index2] = self.order[index2], self.order[index1]

        self.order.append(self.order[0])
        self.calc_fitness()

    def print_path(self):
        """Returns a string representation of the path."""
        path_str = " -> ".join(str(city) for city in self.order[:-1])
            

def cross_over(parent1, parent2):
    k1 = randint(0, len(parent1.order) // 2)
    k2 = randint(len(parent1.order) // 2 + 1, len(parent1.order) - 1)

    if k1 > k2:
        k1, k2 = k2, k1

    # Three-way crossover: child1 gets k1-k2 from parent1, rest from parent2; child2 vice versa
    def create_child(p1, p2):
        middle = p1.order[k1:k2]
        rest = [city for city in p2.order if city not in middle]
        if not rest:
            # If rest is empty, just use middle and repeat the first city
            new_order = middle[:]
        else:
            new_order = [rest[0]] + rest[1:k1] + middle + rest[k1:]
        new_order.append(new_order[0])
        child = CityOrder(new_order)
        child.calc_fitness()
        return child

    child1 = create_child(parent1, parent2)
    child2 = create_child(parent2, parent1)
    return child1, child2
        

