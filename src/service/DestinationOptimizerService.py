import datetime
import json
import string
import time

from src.model.Destination import Destination
from src.util import DistanceUtil
from src.service import OptimizerCore
from src.util import FileUtils


class DestinationOptimizrService:

    def __init__(self):
        self


categories = ['adventure', 'animals', 'arts', 'beach', 'buddhism', 'city', 'cruise', 'drinks', 'elephants', 'food',
              'heritage', 'hiking', 'hunting', 'jungle', 'liquor', 'mountain', 'nature', 'none', 'rafting', 'rivers',
              'safari', 'scenic', 'sea', 'shooting', 'surfing', 'train', 'waterfall']


def get_tuples_from_csv(path: string, selected_categories: []) -> [Destination]:
    data = FileUtils.get_tuples_from_csv(path)

    destinations = []
    for row in data:
        if set(selected_categories) & {row[1], row[3], row[5]}:
            destination = Destination(row[0], row[1], int(row[2]), row[3], int(row[4]), row[5], int(row[6]),
                                      int(row[7]),
                                      int(row[8]), row[9], float(row[10]), float(row[11]))
            destinations.append(destination)
    return destinations


def get_optimized_destinations(selected_categories: []) -> string:
    katunayake = Destination('Katunayake Airport', 'none', 0, 'none', 0, 'none', 0, 'destination', 0, 0,
                             7.180474540914189,
                             79.8833508778138)
    mattala = Destination('Mattala Airport', 'none', 0, 'none', 0, 'none', 0, 'destination', 0, 0, 6.292807024583674,
                          81.12278893160014)

    destinations = DistanceUtil.sort_locations_minimum_distance(
        OptimizerCore.get_optimized_destinations(get_tuples_from_csv('datasets/destinations.csv', selected_categories),
                                                 36, 10000, selected_categories), mattala)

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
