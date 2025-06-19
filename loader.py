# Handles loading the data from file data_tsp.txt
# Each line of the txt file contains the number of the city and its x and y coordinates

def load_cities(file_path):

    cities = {}

    with open(file_path) as f:

        lines = f.readlines()

        for line in lines:

            split_city = line.split()
            print(split_city)
            cities[int(split_city[0])] = [float(split_city[1]), float(split_city[2])]
    
    return cities
