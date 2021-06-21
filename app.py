from flask import Flask
from flask import json
import logging

app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.info("Home page request successful")
    return "Hello World!"

@app.route("/status")
def healthCheck():
    response = app.response_class(
        response=json.dumps({"status": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    app.logger.info("Status Check request successful")
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"status":"success", "data": { "UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info("Metrics check request successful")
    return response

if  __name__ == "__main__":

    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
