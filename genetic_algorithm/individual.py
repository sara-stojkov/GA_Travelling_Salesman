from random import random, randint
from math import sqrt
import matplotlib.pyplot as plt

class CityOrder(object):
    
    # Each city has its number and x and y coordinates, while an individual is an ordered list of cities
    def __init__(self, order):
        """Initializes the CityOrder with a list of cities.
        
        :param order: List of City objects representing the order of cities in the path."""
        self.order = order
        self.fitness = self.calc_fitness()

    def __str__(self): 
        return self.order
    
    def get_fitness(self):
        return self.fitness
    

    def calc_fitness(self):
        """Calculates the fitness of the path, which is the total distance of the path.
        The fitness is calculated as the sum of the distances between consecutive cities in the order."""
        if len(self.order) == 0:
            self.fitness = -1
            return
        path_length = 0
        for i in range (1, len(self.order)):
            distance = sqrt((self.order[i-1].x - self.order[i].x)**2 + (self.order[i-1].y - self.order[i].y)**2)
            path_length += distance

        self.fitness = path_length

    def fill_path_random(self, data):
        """Fills the path with cities in a random order, starting and ending with the same city.
        
        :param data: List of City objects."""

        city_order = []
        
        first_and_last_city = data[randint(0, len(data))-1]
        city_order.append(first_and_last_city)
        all_cities = [city for city in data]
        all_cities.remove(first_and_last_city)
        # data is a list of cities where one element City of a list has:
        # number, x, y
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
        print(f"Path: {path_str}")

    def visualize_path(self):
        """Animates the path traversal using matplotlib."""
        import matplotlib.animation as animation

        x_coords = [city.x for city in self.order]
        y_coords = [city.y for city in self.order]

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set_title('Animated Path Visualization')
        ax.set_xlabel('X Coordinate')
        ax.set_ylabel('Y Coordinate')
        ax.grid()

        # Plot all cities as points
        ax.scatter(x_coords, y_coords, c='blue', marker='o', label='Cities')
        # Mark start/end city
        ax.scatter(x_coords[0], y_coords[0], c='red', marker='s', label='Start/End')

        line, = ax.plot([], [], 'g-', lw=2, label='Path')
        point, = ax.plot([], [], 'ro', markersize=8)

        def init():
            line.set_data([], [])
            point.set_data([], [])
            return line, point

        def update(frame):
            line.set_data(x_coords[:frame+1], y_coords[:frame+1])
            point.set_data([x_coords[frame]], [y_coords[frame]])
            return line, point

        ani = animation.FuncAnimation(
            fig, update, frames=len(self.order), init_func=init,
            interval=400, blit=True, repeat=False
        )

        # Uncomment the next line to save the animation as a GIF
        # ani.save("animation.gif", writer="pillow", fps=5)

        ax.legend()
        plt.show()
            

def cross_over(parent1, parent2, mutation_chance):
    """Performs a three-way crossover between two parents to create two children.
    The crossover is done by selecting two random indices and swapping the segments between them.

    :param parent1: First parent CityOrder object.
    :param parent2: Second parent CityOrder object."""

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

    child1.mutate(mutation_chance)
    child2.mutate(mutation_chance)
    return child1, child2
        

