import math
from src.model import Destination


class DistanceUtil:

    def __init__(self):
        self


def get_distance_between_points(destination1: Destination, destination2: Destination) -> Destination:
    r = 6373.0

    lat1 = math.radians(destination1.lat)
    lon1 = math.radians(destination1.lon)
    lat2 = math.radians(destination2.lat)
    lon2 = math.radians(destination2.lon)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = r * c

    return distance


def sort_locations_minimum_distance(destinations: [Destination], start_point: Destination) -> [Destination]:
    minimum_distance = 0
    sorted_destinations = []
    index_to_pop = 0
    index = 0

    while len(destinations) > 0:

        for current_index, current_destination in enumerate(destinations):
            if index == 0:
                distance = get_distance_between_points(start_point, destinations[current_index])

                if index == 0 and current_index == 0:
                    minimum_distance = distance
                    index_to_pop = current_index
                else:
                    if distance < minimum_distance:
                        minimum_distance = distance
                        index_to_pop = current_index
            else:
                distance = get_distance_between_points(sorted_destinations[len(sorted_destinations) - 1],
                                                       destinations[current_index])

                if current_index == 0:
                    minimum_distance = distance
                    index_to_pop = current_index
                else:
                    if distance < minimum_distance:
                        minimum_distance = distance
                        index_to_pop = current_index

        index = index + 1

        sorted_destinations.append(destinations[index_to_pop])
        destinations.pop(index_to_pop)

    return sorted_destinations
