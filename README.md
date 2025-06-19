# Travelling Salesman Problem (TSP) solved using a Genetic Algorithm

## 📌 Project Description
This repository contains a Python implementation of a Genetic Algorithm (GA) to solve the Travelling Salesman Problem (TSP).

**Problem statement:**
Given a set of cities defined by their coordinates (x, y), the goal is to find the order in which to visit all cities so that:

- each city is visited exactly once,

- the total travel distance is minimized, and

- the tour ends at the starting city.

The distance between two cities is calculated using the Euclidean distance formula:

d(g1, g2) = sqrt( (x1 - x2)^2 + (y1 - y2)^2 )

### 📂 Input Data

File: ```data_tsp.txt```

Each line contains a city’s index and its coordinates.

Example:

```1 10.0 20.0 ```
``` 2 15.0 25.0 ```
...
## 🧬 Genetic Algorithm Overview

This project implements a GA to find a near-optimal route for the TSP.

**Key components:**

### Program structure:

- Reading and parsing input coordinates

- Initial population generation

- Evaluation of fitness (total path length)

- Selection of individuals for crossover

- Crossover operator to generate offspring

- Mutation operator to introduce variation

- Replacement strategy for new generations

- Termination after a set number of generations or convergence

#### Optimality criterion:
The best individual in the population represents the shortest total travel distance found so far.

#### Mutation operator:
Typically, a swap mutation: two cities in the tour are randomly selected and their positions swapped.

#### Crossover operator:
Ordered crossover (OX) or Partially Mapped Crossover (PMX) is commonly used for permutation problems like TSP.

#### Selection strategy:
Tournament selection or roulette wheel selection to choose parents for crossover based on fitness.

- Algorithm parameters:

- Population size

- Number of generations

- Crossover probability

- Mutation probability

## ✅ Results
The output of the algorithm is:

- The best route found (ordered list of cities)

- The total travel distance for this route

Note:
Graphical visualizations or interfaces are not required as per the project specification.

## 📖 Documentation
The project includes documentation in accordance with the standard. It is in the file _documentation/GA_TSP.docx_

- Program structure

- Optimality criterion

- Implementation of mutation and crossover operators

- Selection strategy

- Parameter choices

- Example results

### 🚀 How to Run
Place your data_tsp.txt in the project directory.

Run the Python script:

```python main.py```

The program outputs the best route and its total length.

### ⚙️ Requirements
- Python 3.x

- Standard libraries: random, math, itertools

### 📑 License
This project is intended for educational purposes only.

