import ast
import json

from flask import Flask, jsonify, request

from src.service import DestinationOptimizerService, RestaurantOptimizerService

app = Flask(__name__)


@app.route('/')
def root():
    return DestinationOptimizerService.get_tuples_from_csv()


@app.route('/loadOptimizedDestinations', methods=['POST'])
def get_destinations():
    destination_service = DestinationOptimizerService
    sample = request.get_json()['categories']
    sample.sort(key=lambda x: x["rank"])
    sorted_categories = []
    for category in sample:
        sorted_categories.append(category['title'])
    return jsonify(destination_service.get_optimized_destinations(sorted_categories, request.get_json()['durationOfStay'], request.get_json()['budget']))


@app.route('/loadOptimizedRestaurants')
def get_restaurants():
    restaurant_service = RestaurantOptimizerService
    return jsonify(restaurant_service.load_restaurants())


if __name__ == "__main__":
    app.secret_key = "secret"
    app.debug = True
    app.run()
