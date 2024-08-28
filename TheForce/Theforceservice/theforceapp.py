import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify, request
from service.theforceapiservice import SwapiService
from utils.error_handling import handle_swapi_error

app = Flask(__name__)

log_file = 'logs/theforce.log'
handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
handler.setFormatter(formatter)

app.logger.addHandler(handler)

@app.before_request
def log_request_info():
    app.logger.info('Headers: %s', request.headers)
    app.logger.info('Body: %s', request.get_data())

@app.route('/people', methods=['GET'])
def get_people():
    try:
        people_data = SwapiService.fetch_people_data()
        app.logger.info("SWAPI fetch completed successfully")
        return jsonify(people_data)
    except Exception as e:
        app.logger.error(f"Endpoint Error /people: {str(e)}")
        return handle_swapi_error(e)

if __name__ == '__main__':
    app.logger.setLevel(logging.INFO)
    app.run(debug=True, host='0.0.0.0')



