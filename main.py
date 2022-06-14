from flask import Flask, jsonify

from src.service import DestinationOptimizerService

app = Flask(__name__)


@app.route('/test')
def index():
    destination_service = DestinationOptimizerService
    return jsonify(destination_service.get_optimized_destinations())


app.run()
