# Travelling Salesman Problem (TSP) solved using Genetic Algorithm

## Project Description
This repository contains a Python implementation of a Genetic Algorithm (GA) to solve the Travelling Salesman Problem (TSP).

**Problem statement:**
Given a set of cities defined by their coordinates (x, y), the goal is to find the order in which to visit all cities so that:

- each city is visited exactly once,

- the total travel distance is minimized, and

- the tour ends at the starting city.

The distance between two cities is calculated using the Euclidean distance formula:

```d(g1, g2) = sqrt( (x1 - x2)^2 + (y1 - y2)^2 )```

### Input Data

File: ```data_tsp.txt```

Each line contains a city’s index and its coordinates.

Example:

```1 10.0 20.0 ```

``` 2 15.0 25.0 ```
...

## Genetic Algorithm Overview

This project implements a GA to find a near-optimal route for the TSP.

**Key components:**

### Program structure:

- Reading and parsing input coordinates into _City_ objects

- Initial population generation

- Evaluation of fitness (total path length)

- Choosing parent individuals for crossover

- Crossover operation to generate offspring

- Mutation operator to introduce variation

- Selection of individuals who will survive onto the next generation

- Termination after a set number of generations or convergence to an optimal solution

## Implementation

#### Optimality criterion:
The best individual in the population represents the shortest total travel distance found so far. That is the individual with the smallest _fitness_ score

#### Mutation operator:
Swap operation - mutating a path means swapping n of its cities. The number of cities to swap is variable, between 2 cities and a half of all cities. Adds variability to population.

#### Crossover operator:
Implemented a three-way crossover. Since the cities in a path are a list, after choosing 2 points in those lists (_k1_ and _k2_) two children will inherit those three segments as 1-2-1 and 2-1-2 respectively.

#### Parent selection strategy:
To introduce a bit of randomness but still favour better paths, roulette wheel selection is implemented. Individuals are ranked by fitness, but then also those ranks are multiplied with a random number to generate the final score.

#### Selection:
To determine which paths will move on from this generation onto the next, elitism is applied. Only a few select paths from the parent generation survive and the rest of the population is filled with the best from the children population.

#### Algorithm parameters:
- Population size
- Maximum number of generations
- Mutation probability
- Keep percentage (elitism)

## Results
The output of the algorithm is:
- The best route found (ordered list of cities)
- The total travel distance for this route (fitness of the best individual)

### Achieved results
**Chosen parameters as optimal**:  ```max_generations = 500```, ```population_size = 400```, ```keep_percent = 0.2```, ```mutation_chance = 0.2```. They are based on literature and previous tries of running the algorithm.

For the input data provided, the results for the length of the shortest path are typically between 8000 and 9000, the best was around 8249.

In the ```individual.py``` there is also a function which handles visualizing a path (solution) by an animation showed below.

![animation](https://github.com/user-attachments/assets/fae219d5-eb8e-4317-8728-195a1b3085e8)

#### Other solution examples
Here are provided other solutions achieved with these parameters. They may look alike but that is expected since the input cities are the same, so some sequences are expected to be similar.
<img width="1250" height="800" alt="image" display="inline" src="https://github.com/user-attachments/assets/8c3e5a16-a4e7-42a6-a2b4-5b5511e2e3e4" />

<img width="1250" height="800" alt="image" display="inline" src="https://github.com/user-attachments/assets/5e1268d6-a205-43d4-ad3f-5b061c7274e3" />


### 🚀 How to Run
1. Place your data_tsp.txt in the project directory.
2. Run the Python script:
```python main.py```

The program outputs the best route and its total length, as well as the visualization of that path

### ⚙️ Requirements
- Python 3.x
- _matplotlib_ for visualization
  
- Standard libraries: random, math, statistics

### 📑 License
This project is intended for educational purposes only.

