# This module will contain all data concerning the Genetic Algorithm - defining the initial generation, fitness function,
# and mutations

from statistics import mean, median
from genetic_algorithm.individual import CityOrder, cross_over
import random

        
# A generation or population is a group of many individuals
    # add funtions for selection, crossover and mutations


def selection(population, new_population, keep_percent, population_size):
    """    Selects the best individuals from the current population and the new population.
    The best individuals are kept based on the keep_percent parameter.
    The new population is created by combining the best individuals from both populations.

    :param population: Current population of CityOrder objects.
    :param new_population: New population (children) of CityOrder objects.
    :param keep_percent: Percentage of the best individuals to keep from the current population.
    :param population_size: Total size of the population after selection.
    """
    final_gen = []
    population.sort(reverse=False, key= lambda CityOrder: CityOrder.get_fitness())
    to_keep_old = int(population_size * keep_percent)
    new_gen_to_add = population_size - to_keep_old
    new_population.sort(reverse=False, key= lambda CityOrder: CityOrder.get_fitness())
    final_gen = population[:to_keep_old] + new_population[:new_gen_to_add]

    return final_gen

def parent_selection(population):
    """
    Selects two parents from the population for crossover
    using weighted random scoring.

    :param population: List of CityOrder objects representing the current population.
    """
    fitness_scores = [ind.get_fitness() for ind in population]
    random_scores = [random.random() for _ in range(len(fitness_scores))]
    final_scores = [
        (i, fitness_scores[i] * random_scores[i])
        for i in range(len(fitness_scores))
    ]
    # sort by the random-weighted scores
    final_scores.sort(key=lambda x: x[1])   
    parent1 = population[final_scores[0][0]]
    parent2 = population[final_scores[1][0]]
    return parent1, parent2

def crossover_all(population, population_size, mutation_chance):
    """Performs crossover on the entire population to create a new generation of individuals.

    :param population: List of CityOrder objects representing the current population.
    :param population_size: Size of the population for the next generation.
    :param mutation_chance: Chance of mutation for each new individual.
    """

    child_gen = []

    while len(child_gen) < population_size:
        parent1, parent2 = parent_selection(population)

        child1, child2 = cross_over(parent1, parent2, mutation_chance)
        child_gen.append(child1)
        child_gen.append(child2)

    return child_gen
    

def initial_population(size, data):
    """Populates the first generation with paths.

    :param size: Size of the initial population.
    :param data: List of City objects representing all the cities."""
    population = []
    for i in range(size):
        path = CityOrder([])
        path.fill_path_random(data)

        population.append(path)

    return population




# The idea is to start with initial population and then go through a cycle of selection, breeding and mutating (then calculating the fitness)
def life_cycle(data, population_size, keep_percent, mutations_chance, max_generations):
    """Runs the life cycle of the genetic algorithm, starting with an initial population and going through generations.

    :param data: List of City objects representing the cities.
    :param population_size: Size of the population for each generation.
    :param keep_percent: Percentage of the best individuals to keep from the current population.
    :param mutations_chance: Chance of mutation for each individual.
    :param max_generations: Maximum number of generations to run the algorithm."""
    
    current_gen = initial_population(population_size, data)

    gen_counter = 1

    # should add another stop criteria, maybe optional
    while gen_counter < max_generations:
        new_gen = crossover_all(current_gen, population_size, mutations_chance)
        current_gen = selection(current_gen, new_gen, keep_percent, population_size)
        # Mutations happen in crossover on new individuals
        display_generation(current_gen, gen_counter)
        gen_counter += 1
    
    current_gen.sort(reverse=False, key=lambda CityOrder:CityOrder.fitness)
    print("Best path found after", gen_counter, "generations:")
    print("Path length:", current_gen[0].get_fitness())
    print(current_gen[0].print_path())
    current_gen[0].visualize_path()


def display_generation(generation, generation_number):
    """Prints out the 'stats' of a generation, for debugging and process tracking purposes."""
    fitness_sum = []
    for individual in generation:
        fitness_sum.append(individual.fitness)

    f_mean = mean(fitness_sum)
    f_median = median(fitness_sum)

    print("-----------------------\n Generation number", generation_number)
    print("Generation mean", f_mean)
    print("Generation median", f_median)
    print("Generation best fitness", min(fitness_sum))
    print("")

def plot_results():
    pass