# This module will contain all data concerning the Genetic Algorithm - defining the initial generation, fitness function,
# and mutations

from const import POPULATION_SIZE, PERCENT_TO_KEEP, MUTATION_CHANCE
from math import sqrt
from statistics import mean, median

class individual(object):
    
    # Each city has its number and x and y coordinates, while an individual is an ordered list of cities
    def __init__(self, order):
        self.order = order
        self.fitness = self.fitness()

    def fitness(self):
        path_length = 0
        for i in range (1, len(self.order)):
            distance = sqrt((self.order[i-1].x - self.order[i].x)**2 + (self.order[i-1].y - self.order[i].y)**2)
            path_length += distance

    def mate(self, other): 
        baby = []

    def mutate(self, chance=MUTATION_CHANCE):
        for city in self.order:
            pass

        
# A generation or population is a group of many individuals
class generation(object):
    # add funtions for selection, crossover and mutations
    def __init__ (self, population):
        self.population = population

    def selection(self):
        self.population.sort(reverse=True, key=individual.fitness())
        to_keep = POPULATION_SIZE * PERCENT_TO_KEEP
        new_population = self.population[:to_keep]

        return new_population
    
    def crossover(self):
        pass
        

    def mutations(self):

        for individual in self.population:
            individual.mutate()

        return self.population


# First population should be 
def initial_population(size, data):
    pass

# The idea is to start with initial population and then go through a cycle of selection, breeding and mutating (then calculating the fitness)
def life_cycle(data, population_size, keep_percent, mutations_chance, max_generations, stop_criteria):
    
    current_gen = initial_population(population_size, data)

    gen_counter = 1

    # should add another stop criteria, maybe optional
    while gen_counter < max_generations:
        current_gen.selection(keep_percent)
        current_gen.crossover(population_size)
        current_gen.mutations(mutations_chance)



def display_generation(generation):
    fitness_sum = 0
    for individual in generation:
        fitness_sum.append(individual.fitness)

    f_mean = mean(fitness_sum)
    f_median = median(fitness_sum)

    print("-----------------------\n Generation number", generation.number)
    print("Generation mean", f_mean)
    print("Generation median", f_median)
    print("Generation best fitness", max(fitness_sum))
    print("")

def plot_results():
    pass