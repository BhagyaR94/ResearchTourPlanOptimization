import string
from functools import partial
from random import choices, randint, randrange, random
from typing import List, Callable, Tuple

from src.model.Destination import Destination


class OptimizerCore:
    def __init__(self):
        self


Genome = List[int]  # genome is a list of integers
Population = List[Genome]  # population is a list of genomes
FitnessFunc = Callable[[Genome], int]
PopulateFunc = Callable[[], Population]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossOverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]


def __generate_genome(length: int) -> Genome:
    return choices([0, 1], k=length)


def __generate_population(size: int, genome_length: int) -> Population:
    return [__generate_genome(genome_length) for _ in range(size)]


def __fitness_destinations(genome: Genome, destinations: [Destination], time_limit: int, price_limit: int,
                           selected_categories: []) -> int:
    if len(genome) != len(destinations):
        raise ValueError("genome and destinations must match and be of same length")

    duration = 0
    value = 0
    price = 0

    for i, destination in enumerate(destinations):
        if genome[i] == 1:
            duration += destination.time
            value += __get_value(selected_categories, destination)
            price += destination.price

            if (duration > time_limit) | (price > price_limit):
                return 0

    return value


def __get_value(selected_categories: [], destination: Destination) -> int:
    total_value = 0
    if set(selected_categories) & {destination.category1}:
        total_value += destination.category1_value

    if set(selected_categories) & {destination.category2}:
        total_value += destination.category2_value

    if set(selected_categories) & {destination.category3}:
        total_value += destination.category3_value

    return int(total_value / len(selected_categories))


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


def __genome_to_things(genome: Genome, things: [Destination]) -> [Destination]:
    result = []
    for i, thing in enumerate(things):
        if genome[i] == 1:
            result += [thing]

    return result


def get_optimized_destinations(more_destinations: [Destination], time_limit: int, price_limit: int,
                               selected_categories: []) -> [string]:
    # start = time.time()

    population, generations = __run_evolution(
        populate_func=partial(
            __generate_population, size=10, genome_length=len(more_destinations)
        ),
        fitness_func=partial(
            __fitness_destinations, destinations=more_destinations, time_limit=time_limit, price_limit=price_limit,
            selected_categories=selected_categories
        ),
        fitness_limit=3000,
        generation_limit=100
    )

    # end = time.time()
    #
    # print(f"time: {end - start}s")

    return __genome_to_things(population[0], more_destinations)


def get_optimized_restaurants(more_destinations: [Destination], time_limit: int, price_limit: int) -> [string]:
    population, generations = __run_evolution(
        populate_func=partial(
            __generate_population, size=10, genome_length=len(more_destinations)
        ),
        fitness_func=partial(
            __fitness_destinations, destinations=more_destinations, time_limit=time_limit, price_limit=price_limit
        ),
        fitness_limit=2000,
        generation_limit=1000
    )

    return __genome_to_things(population[0], more_destinations)


def get_optimized_hotels(more_destinations: [Destination], time_limit: int, price_limit: int) -> [string]:
    population, generations = __run_evolution(
        populate_func=partial(
            __generate_population, size=10, genome_length=len(more_destinations)
        ),
        fitness_func=partial(
            __fitness_destinations, destinations=more_destinations, time_limit=time_limit, price_limit=price_limit
        ),
        fitness_limit=2000,
        generation_limit=1000
    )

    return __genome_to_things(population[0], more_destinations)
