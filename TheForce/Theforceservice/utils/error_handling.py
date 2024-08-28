from flask import jsonify

def handle_swapi_error(e):
    response = jsonify({"error": str(e)})
    response.status_code = 500
    return response
