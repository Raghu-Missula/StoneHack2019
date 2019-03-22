
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, make_response, request, jsonify
import sys

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    print(req, file=sys.stderr)
    return make_response(jsonify({'fulfillmentText':'Your next pill is at 7pm'}))

