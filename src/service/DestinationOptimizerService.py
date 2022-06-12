import string

from src.model.Destination import Destination

import time
from functools import partial
from random import choices, randint, randrange, random
from typing import List, Callable, Tuple


class DestinationOptimizrService:

    def __init__(self):
        self


Genome = List[int]  # genome is a list of integers
Population = List[Genome] # population is a list of genomes
FitnessFunc = Callable[[Genome], int]
PopulateFunc = Callable[[], Population]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossOverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]

more_destinations = [
    Destination('Yala Safari', 5, 5, 500, 'destination', 0, 0),
    Destination('Dambulla Rock Temple', 10, 2, 100, 'destination', 0, 0),
    Destination('Nuwara Eliya City Tour', 15, 1, 50, 'destination', 0, 0),
    Destination('Kandy Temple Of Tooth', 500, 1, 200, 'destination', 0, 0),
    Destination('Train from Kandy to Ella', 100, 6, 300, 'destination', 0, 0),
    Destination('Ella Eco Hike', 600, 8, 500, 'destination', 0, 0),
    Destination('Sigiriya', 170, 3, 800, 'destination', 0, 0),
    Destination('Dunhinda', 60, 1, 200, 'destination', 0, 0),
    Destination('Mirissa Whale Watching', 60, 6, 1000, 'destination', 0, 0),
    Destination('Arugam Bay Surfing', 30, 4, 100, 'destination', 0, 0),
]


def __generate_genome(length: int) -> Genome:
    return choices([0, 1], k=length)


def __generate_population(size: int, genome_length: int) -> Population:
    return [__generate_genome(genome_length) for _ in range(size)]


def __fitness(genome: Genome, destinations: [Destination], time_limit: int, price_limit: int) -> int:
    if len(genome) != len(destinations):
        raise ValueError("genome and destinations must match and be of same length")

    duration = 0
    value = 0
    price = 0

    for i, destination in enumerate(destinations):
        if genome[i] == 1:
            duration += destination.time
            value += destination.value
            price += destination.price

            if (duration > time_limit) | (price > price_limit):
                return 0

    return value


def __selection_pair(population: Population, fitness_func: FitnessFunc) -> Population:
    return choices(
        population=population,
        weights=[fitness_func(genome) for genome in population],
        k=2
    )


def __single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
    if len(a) != len(b):
        raise ValueError("a and B must be of same length")

    length = len(a)
    if length < 2:
        return a, b

    p = randint(1, length - 1)
    return a[0:p] + b[p:], b[0:p] + a[p:]


def __mutation(genome: Genome, num: int = 1, probability: float = 0.5) -> Genome:
    for _ in range(num):
        index = randrange(len(genome))
        genome[index] = genome[index] if random(
        ) > probability else abs(genome[index] - 1)
    return genome


def __run_evolution(
        populate_func: PopulateFunc,
        fitness_func: FitnessFunc,
        fitness_limit: int,
        selection_func: SelectionFunc = __selection_pair,
        crossover_func: CrossOverFunc = __single_point_crossover,
        mutation_func: MutationFunc = __mutation,
        generation_limit: int = 1000
) -> Tuple[Population, int]:
    population = populate_func()

    for i in range(generation_limit):
        population = sorted(
            population,
            key=lambda genome: fitness_func(genome),
            reverse=True
        )

        if fitness_func(population[0]) >= fitness_limit:
            break
        next_generation = population[0: 2]

        for j in range(int(len(population) / 2) - 1):
            parents = selection_func(population, fitness_func)
            offspring_a, offspring_b = crossover_func(parents[0], parents[1])
            offspring_a = mutation_func(offspring_a)
            offspring_b = mutation_func(offspring_b)
            next_generation += [offspring_a, offspring_b]

        population = next_generation

    population = sorted(
        population,
        key=lambda genome: fitness_func(genome),
        reverse=True
    )
    return population, i


population, generations = __run_evolution(
    populate_func=partial(
        __generate_population, size=10, genome_length=len(more_destinations)
    ),
    fitness_func=partial(
        __fitness, destinations=more_destinations, time_limit=24, price_limit=10000
    ),
    fitness_limit=2000,
    generation_limit=1000
)


def __genome_to_things(genome: Genome, things: [Destination]) -> [Destination]:
    result = []
    for i, thing in enumerate(things):
        if genome[i] == 1:
            result += [thing.name]

    return result


def get_optimized_destinations() -> [string]:
    return __genome_to_things(population[0], more_destinations)


def bestTimes(genome: Genome, things: [Destination]) -> [Destination]:
    result = []
    for i, thing in enumerate(things):
        if genome[i] == 1:
            result += [thing.time]

    return result


def bestCosts(genome: Genome, things: [Destination]) -> [Destination]:
    result = []
    for i, thing in enumerate(things):
        if genome[i] == 1:
            result += [thing.price]

    return result


def genome_to_things_two(genome: Genome, things: [Destination]) -> [Destination]:
    result = 0
    for i, thing in enumerate(things):
        if genome[i] == 1:
            result += thing.price

    return result


def genome_to_things_three(genome: Genome, things: [Destination]) -> [Destination]:
    result = 0
    for i, thing in enumerate(things):
        if genome[i] == 1:
            result += thing.time

    return result


def genome_to_things_four(genome: Genome, things: [Destination]) -> [Destination]:
    result = 0
    for i, thing in enumerate(things):
        if genome[i] == 1:
            result += thing.value

    return result


# print(f"number of generations: {generations}")
# print(f"time: {end - start}s")

# print(f"best solution: {genome_to_things(population[0], more_destinations)}")

# print(f"times: {bestTimes(population[0], more_destinations)}")
# print(f"costs: {bestCosts(population[0], more_destinations)}")
# print(f"Total Cost: {genome_to_things_two(population[0], more_destinations)}")
# print(f"Total Time: {genome_to_things_three(population[0], more_destinations)}")
# print(f"Total Value: {genome_to_things_four(population[0], more_destinations)}")
