import string

from src.model.Destination import Destination
from src.service import OptimizerCore
from src.util import DistanceUtil
from src.util import FileUtils


class DestinationOptimizrService:

    def __init__(self):
        self


def get_tuples_from_csv(path: string, selected_categories: []) -> [Destination]:
    data = FileUtils.get_tuples_from_csv(path)

    category1_destinations = []
    category2_destinations = []
    category3_destinations = []
    for row in data:
        if selected_categories[0] == row[1]:
            destination = Destination(row[0], row[1], int(row[2]), row[3], int(row[4]), row[5], int(row[6]),
                                      int(row[7]),
                                      int(row[8]), row[9], float(row[10]), float(row[11]))
            category1_destinations.append(destination)
        if selected_categories[1] == row[1]:
            destination = Destination(row[0], row[1], int(row[2]), row[3], int(row[4]), row[5], int(row[6]),
                                      int(row[7]),
                                      int(row[8]), row[9], float(row[10]), float(row[11]))
            category2_destinations.append(destination)
        if selected_categories[2] == row[1]:
            destination = Destination(row[0], row[1], int(row[2]), row[3], int(row[4]), row[5], int(row[6]),
                                      int(row[7]),
                                      int(row[8]), row[9], float(row[10]), float(row[11]))
            category3_destinations.append(destination)
    return [category1_destinations, category2_destinations, category3_destinations]


def get_optimized_destinations(selected_categories: [], duration_of_stay: int, budget: int) -> string:
    katunayake = Destination('Katunayake Airport', 'none', 0, 'none', 0, 'none', 0, 'destination', 0, 0,
                             7.180474540914189,
                             79.8833508778138)
    mattala = Destination('Mattala Airport', 'none', 0, 'none', 0, 'none', 0, 'destination', 0, 0, 6.292807024583674,
                          81.12278893160014)

    category1 = get_tuples_from_csv('datasets/destinations.csv', selected_categories)[0]
    category2 = get_tuples_from_csv('datasets/destinations.csv', selected_categories)[1]
    category3 = get_tuples_from_csv('datasets/destinations.csv', selected_categories)[2]

    optimized_destinations_cat1 = OptimizerCore.get_optimized_destinations(category1,
                                                                           ((duration_of_stay * 50) / 100),
                                                                           ((budget * 50) / 100), selected_categories)

    optimized_destinations_cat2 = OptimizerCore.get_optimized_destinations(category2,
                                                                           ((duration_of_stay * 30) / 100),
                                                                           ((budget * 30) / 100), selected_categories)

    optimized_destinations_cat3 = OptimizerCore.get_optimized_destinations(category3,
                                                                           ((duration_of_stay * 20) / 100),
                                                                           ((budget * 20) / 100), selected_categories)

    destinations = DistanceUtil.sort_locations_minimum_distance(
        (optimized_destinations_cat1 + optimized_destinations_cat2 + optimized_destinations_cat3), mattala)

    objects = []
    for destination in destinations:
        objects.append(
            {
                'destinationName': destination.name,
                'destinationCategory1': destination.category1,
                'destinationCategory2': destination.category2,
                'destinationCategory3': destination.category3,
                'destinationDurationToCover': destination.time,
                'destinationCost': destination.price,
                'destinationType': destination.type,
                'destinationLatitude': destination.lat,
                'destinationLongitude': destination.lon
            }
        )

    return objects
