from loader import load_cities
from genetic_algorithm.generations import life_cycle
from const import DATA_FILE_PATH, POPULATION_SIZE, PERCENT_TO_KEEP, MUTATION_CHANCE, MAX_GENERATIONS

cities = load_cities(DATA_FILE_PATH)

life_cycle(data=cities, population_size=POPULATION_SIZE, keep_percent=PERCENT_TO_KEEP, 
           mutations_chance=MUTATION_CHANCE, max_generations=MAX_GENERATIONS)