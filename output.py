first_coordinate = [565, 25, 345, 945, 845, 880, 25, 525, 580, 650, 1605, 1220, 1465, 1530, 845, 725, 145, 415, 510, 560]
second_coordinate = [575, 185, 750, 685, 655, 660, 230, 1000, 1175, 1130, 620, 580, 200, 5, 680, 370, 665, 635, 875, 365]

class City:

     def __init__(self, first_coordinate, second_coordinate):
         self.first_coordinate = first_coordinate
         self.second_coordinate = second_coordinate

     def distance(self, City):
         if self.first_coordinate - city.first_coordinate > 0:
             distance_on_first_coordinate = self.first_coordinate - city.first_coordinate
         else:
             distance_on_first_coordinate = city.first_coordinate - self.first_coordinate
         if self.second_coordinate - city.second_coordinate > 0:
             distance_on_second_coordinate = self.second_coordinate - city.second_coordinate
         else:
             distance_on_second_coordinate = city.second_coordinate - self.second_coordinate
         distance = distance_on_first_coordinate + distance_on_second_coordinate
         return distance

class Conformity:

     def __init__(self, route):
         self.route = route
         self.distance = 0
         self.conformity = 0

     def distance_on_route(self):
         if self.distance == 0:
             distance = 0
             for i in range(0, len(self.route) - 1):
                 start_city = self.route[i]
                 finish_city = self.route[i+1]
                 distance = distance + start_city.distance(finish_city)
             self.distance = distance
         return self.distance

     def route_conformity(self):
         if self.conformity == 0:
             distance = self.distance_on_route
             self.conformity = 1 / distance
         return self.conformity

city_list = []
for i in range(0, len(first_coordinate)):
     xi = first_coordinate[i]
     yi = second_coordinate[i]
     new_city = City(xi, yi)
     city_list.append(new_city)

def population_creation(population_magnitude, city_list):
     population = []
     for i in range(0, population_magnitude):
         route = route_creation(city_list)
         population.append(route)
     return population

def pool_creation(population, selection_results):
     pool = []
     for i in range(0, len(selection_results)):
         j = selection_results[i]
         pool.append(population[j])
     return pool

def descendant(first_parent, second_parent):
     descendant = []
     left_descendant = []
     right_descendant = []
     first_gene = int(random.random() * len(first_parent))
     second_gene = int(random.random() * len(second_parent))
     elementary_gene = min(first_gene, second_gene)
     finite_gene = max(first_gene, second_gene)
     for i in range(elementary_gene, finite_gene):
         left_descendant.append(first_parent[i])
     for letter in second_parent:
         if letter  not in left_descendant:
             right_descendant.append(letter)
     descendant = left_descendant + right_descendant
     return descendant

def mutation(individual, mutation_speed):
     for i in range(0, len(individual)):
         if random.random() < mutation_speed:
             j = int(random.random() * len(individual))
             first_city = individual[i]
             second_city = individual[j]
             individual[i] = second_city
             individual[j] = first_city
     return individual

def population_mutation(population, mutation_speed):
     mutant_population = []
     for i in range(0, len(population)):
         mutant = mutation(population[i], mutation_speed)
         mutant_population.append(mutant)
     return mutant_population
