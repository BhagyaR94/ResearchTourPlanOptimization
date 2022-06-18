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
    return jsonify(destination_service.get_optimized_destinations(ast.literal_eval(request.get_json()['category'])))


@app.route('/loadOptimizedRestaurants')
def get_restaurants():
    restaurant_service = RestaurantOptimizerService
    return jsonify(restaurant_service.load_restaurants())


if __name__ == "__main__":
    app.secret_key = "secret"
    app.debug = True
    app.run()
