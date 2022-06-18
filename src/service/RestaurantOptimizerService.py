import string

from src.model.Destination import Destination
from src.util import FileUtils


class RestaurantOptimizerService:
    def __init__(self):
        self


def get_tuples_from_csv(path: string) -> [Destination]:
    data = FileUtils.get_tuples_from_csv(path)

    restaurants = []
    for row in data:
        restaurant = Destination(row[0], int(row[1]), int(row[2]), int(row[3]), row[4], float(row[5]),
                                 float(row[6]))
        restaurants.append(restaurant)

    return restaurants


def load_restaurants():
    return get_tuples_from_csv('datasets/restaurants_2.csv')
