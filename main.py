from loader import load_cities
from genetic_algorithm.generations import life_cycle
from const import POPULATION_SIZE, PERCENT_TO_KEEP, MUTATION_CHANCE

print(load_cities)

life_cycle()