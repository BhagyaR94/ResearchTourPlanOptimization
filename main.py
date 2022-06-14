from flask import Flask, jsonify

from src.service import DestinationOptimizerService

app = Flask(__name__)


@app.route('/')
def root():
    return 'hello'


@app.route('/test')
def index():
    destination_service = DestinationOptimizerService
    return jsonify(destination_service.get_optimized_destinations())


if __name__ == "__main__":
    app.secret_key = "secret"
    app.debug = True
    app.run()
