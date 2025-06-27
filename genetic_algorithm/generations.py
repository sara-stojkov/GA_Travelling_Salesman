# This module will contain all data concerning the Genetic Algorithm - defining the initial generation, fitness function,
# and mutations

from statistics import mean, median
from individual import CityOrder

        
# A generation or population is a group of many individuals
    # add funtions for selection, crossover and mutations


def selection(population, population_size, keep_percent):
    population.sort(reverse=True, key= lambda CityOrder: CityOrder.get_fitness())
    to_keep = population_size * keep_percent
    new_population = population[:to_keep]

    return new_population

def crossover(population):
    pass
    

def initial_population(size, data):
    """Populates the first generation with paths."""
    population = []
    for i in range(size):
        path = CityOrder()
        path.fill_path_random(data)

        population.append(path)

    return population




# The idea is to start with initial population and then go through a cycle of selection, breeding and mutating (then calculating the fitness)
def life_cycle(data, population_size, keep_percent, mutations_chance, max_generations, stop_criteria):
    
    current_gen = initial_population(population_size, data)

    gen_counter = 1

    # should add another stop criteria, maybe optional
    while gen_counter < max_generations:
        selection(current_gen, keep_percent)
        crossover(current_gen, population_size)
        # Mutations happen in crossover on new individuals


def display_generation(generation):
    """Prints out the 'stats' of a generation, for debugging and process tracking purposes."""
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