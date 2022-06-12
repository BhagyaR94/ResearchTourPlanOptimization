# import math
# import time
# from functools import partial
# from random import choices, randint, randrange, random
# from typing import List, Callable, Tuple
#
# from src.model.Destination import Destination
#
# Genome = List[int]
# Population = List[Genome]
# FitnessFunc = Callable[[Genome], int]
# PopulateFunc = Callable[[], Population]
# SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
# CrossOverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
# MutationFunc = Callable[[Genome], Genome]
#
# more_destinations = [
#     Destination('Yala Safari', 5, 5, 500, 'destination', 0, 0),
#     Destination('Dambulla Rock Temple', 10, 2, 100, 'destination', 0, 0),
#     Destination('Nuwara Eliya City Tour', 15, 1, 50, 'destination', 0, 0),
#     Destination('Kandy Temple Of Tooth', 500, 1, 200, 'destination', 0, 0),
#     Destination('Train from Kandy to Ella', 100, 6, 300, 'destination', 0, 0),
#     Destination('Ella Eco Hike', 600, 8, 500, 'destination', 0, 0),
#     Destination('Sigiriya', 170, 3, 800, 'destination', 0, 0),
#     Destination('Dunhinda', 60, 1, 200, 'destination', 0, 0),
#     Destination('Mirissa Whale Watching', 60, 6, 1000, 'destination', 0, 0),
#     Destination('Arugam Bay Surfing', 30, 4, 100, 'destination', 0, 0),
# ]
#
#
# def get_distance_between_points(destination1: Destination, destination2: Destination) -> Destination:
#     r = 6373.0
#
#     lat1 = math.radians(destination1.lat)
#     lon1 = math.radians(destination1.lon)
#     lat2 = math.radians(destination2.lat)
#     lon2 = math.radians(destination2.lon)
#
#     dlon = lon2 - lon1
#     dlat = lat2 - lat1
#
#     a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
#     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
#
#     distance = r * c
#
#     print("Result:", distance)
#     print("Should be:", 278.546, "km")
#     return 0;
#
#
# def generate_genome(length: int) -> Genome:
#     return choices([0, 1], k=length)
#
#
# def generate_population(size: int, genome_length: int) -> Population:
#     return [generate_genome(genome_length) for _ in range(size)]
#
#
# def fitness(genome: Genome, destinations: [Destination], time_limit: int, price_limit: int) -> int:
#     if len(genome) != len(destinations):
#         raise ValueError("genome and destinations must match and be of same length")
#
#     time = 0
#     value = 0
#     price = 0
#
#     for i, destination in enumerate(destinations):
#         if genome[i] == 1:
#             time += destination.time
#             value += destination.value
#             price += destination.price
#
#             if (time > time_limit) | (price > price_limit):
#                 return 0
#
#     return value
#
#
# def selection_pair(population: Population, fitness_func: FitnessFunc) -> Population:
#     return choices(
#         population=population,
#         weights=[fitness_func(genome) for genome in population],
#         k=2
#     )
#
#
# def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
#     if len(a) != len(b):
#         raise ValueError("a and B must be of same length")
#
#     length = len(a)
#     if length < 2:
#         return a, b
#
#     p = randint(1, length - 1)
#     return a[0:p] + b[p:], b[0:p] + a[p:]
#
#
# def mutation(genome: Genome, num: int = 1, probability: float = 0.5) -> Genome:
#     for _ in range(num):
#         index = randrange(len(genome))
#         genome[index] = genome[index] if random(
#         ) > probability else abs(genome[index] - 1)
#     return genome
#
#
# def run_evolution(
#         populate_func: PopulateFunc,
#         fitness_func: FitnessFunc,
#         fitness_limit: int,
#         selection_func: SelectionFunc = selection_pair,
#         crossover_func: CrossOverFunc = single_point_crossover,
#         mutation_func: MutationFunc = mutation,
#         generation_limit: int = 1000
# ) -> Tuple[Population, int]:
#     population = populate_func()
#
#     for i in range(generation_limit):
#         population = sorted(
#             population,
#             key=lambda genome: fitness_func(genome),
#             reverse=True
#         )
#
#         if fitness_func(population[0]) >= fitness_limit:
#             break
#         next_generation = population[0: 2]
#
#         for j in range(int(len(population) / 2) - 1):
#             parents = selection_func(population, fitness_func)
#             offspring_a, offspring_b = crossover_func(parents[0], parents[1])
#             offspring_a = mutation_func(offspring_a)
#             offspring_b = mutation_func(offspring_b)
#             next_generation += [offspring_a, offspring_b]
#
#         population = next_generation
#
#     population = sorted(
#         population,
#         key=lambda genome: fitness_func(genome),
#         reverse=True
#     )
#     return population, i
#
#
# start = time.time()
# population, generations = run_evolution(
#     populate_func=partial(
#         generate_population, size=10, genome_length=len(more_destinations)
#     ),
#     fitness_func=partial(
#         fitness, destinations=more_destinations, time_limit=24, price_limit=10000
#     ),
#     fitness_limit=2000,
#     generation_limit=1000
# )
# end = time.time()
#
#
# def genome_to_things(genome: Genome, things: [Destination]) -> [Destination]:
#     result = []
#     for i, thing in enumerate(things):
#         if genome[i] == 1:
#             result += [thing.name]
#
#     return result
#
#
# def bestTimes(genome: Genome, things: [Destination]) -> [Destination]:
#     result = []
#     for i, thing in enumerate(things):
#         if genome[i] == 1:
#             result += [thing.time]
#
#     return result
#
#
# def bestCosts(genome: Genome, things: [Destination]) -> [Destination]:
#     result = []
#     for i, thing in enumerate(things):
#         if genome[i] == 1:
#             result += [thing.price]
#
#     return result
#
#
# def genome_to_things_two(genome: Genome, things: [Destination]) -> [Destination]:
#     result = 0
#     for i, thing in enumerate(things):
#         if genome[i] == 1:
#             result += thing.price
#
#     return result
#
#
# def genome_to_things_three(genome: Genome, things: [Destination]) -> [Destination]:
#     result = 0
#     for i, thing in enumerate(things):
#         if genome[i] == 1:
#             result += thing.time
#
#     return result
#
#
# def genome_to_things_four(genome: Genome, things: [Destination]) -> [Destination]:
#     result = 0
#     for i, thing in enumerate(things):
#         if genome[i] == 1:
#             result += thing.value
#
#     return result
#
#
# # print(f"number of generations: {generations}")
# # print(f"time: {end - start}s")
#
# print(f"best solution: {genome_to_things(population[0], more_destinations)}")
# # print(f"times: {bestTimes(population[0], more_destinations)}")
# # print(f"costs: {bestCosts(population[0], more_destinations)}")
# # print(f"Total Cost: {genome_to_things_two(population[0], more_destinations)}")
# # print(f"Total Time: {genome_to_things_three(population[0], more_destinations)}")
# # print(f"Total Value: {genome_to_things_four(population[0], more_destinations)}")

from src.service import DestinationOptimizerService
destinationOptimizer = DestinationOptimizerService
