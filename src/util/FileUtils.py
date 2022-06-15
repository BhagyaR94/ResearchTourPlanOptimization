import csv
import string
from collections import namedtuple

from src.model.Destination import Destination


class FileUtils:
    def __init__(self):
        self


def get_tuples_from_csv(file_path: string) -> string:
    with open(file_path, newline='') as file:
        reader = csv.reader(file)

        header = []
        header = next(reader)
        header

        data = []
        for row in reader:
            data.append(row)

    return data
