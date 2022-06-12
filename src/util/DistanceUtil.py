import math
from src.model import Destination


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

    print("Result:", distance)
    print("Should be:", 278.546, "km")
    return distance;