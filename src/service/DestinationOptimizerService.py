import string

from src.model.Destination import Destination
from src.util import DistanceUtil

from src.service import OptimizerCore


class DestinationOptimizrService:

    def __init__(self):
        self


more_destinations = [
    Destination('Yala Safari', 5, 5, 500, 'destination', 6.3686384758281624, 81.51745180675918),
    Destination('Dambulla Rock Temple', 10, 2, 100, 'destination', 7.856799710633441, 80.64900760288403),
    Destination('Nuwara Eliya City Tour', 15, 1, 50, 'destination', 6.9494905173802515, 80.78558115275386),
    Destination('Kandy Temple Of Tooth', 500, 1, 200, 'destination', 7.293811176348765, 80.64173267217323),
    Destination('Train from Kandy to Ella', 100, 6, 300, 'destination', 7.289468405771871, 80.63190367572007),
    Destination('Ella Eco Hike', 600, 8, 500, 'destination', 6.866629755612183, 81.04644578358516),
    Destination('Sigiriya', 170, 3, 800, 'destination', 7.958758044344503, 80.76045722332174),
    Destination('Dunhinda', 60, 1, 200, 'destination', 7.017722702597019, 81.06388734147676),
    Destination('Mirissa Whale Watching', 60, 6, 1000, 'destination', 5.94911871048566, 80.44879552605009),
    Destination('Arugam Bay Surfing', 30, 4, 100, 'destination', 6.838134259204478, 81.82617002477654),
]


def get_optimized_destinations() -> [string]:
    start_point = Destination('Katunayake Airport', 0, 0, 0, 'destination', 7.180474540914189, 79.8833508778138)
    optimized_destinations = OptimizerCore.get_optimized_destinations(more_destinations, 24, 10000)

    for opts in optimized_destinations:
        print('opts - ', opts.name)

    sorted_dests = DistanceUtil.sort_locations_minimum_distance(optimized_destinations, start_point)

    for sorts in sorted_dests:
        print('sorts - ', sorts.name)

    # return DistanceUtil.sort_locations_minimum_distance(optimized_destinations, start_point)
