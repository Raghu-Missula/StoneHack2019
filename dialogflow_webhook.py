

from flask import Flask, make_response, request, jsonify
import requests
import time
import json
import sys

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    c = requests.get("https://stonehill-hackathon.firebaseio.com/timestamps.json")
    tempStamps = json.loads(c.json())
    lowest_stamps = [tempStamps[key][0] for key in tempStamps.keys()]
    medicineName = list(tempStamps.keys())[lowest_stamps.index(min(lowest_stamps))]
    req = request.get_json(force=True)
    print(req, file=sys.stderr)
    timeStamp = time.asctime(time.localtime(min(lowest_stamps)))
    timeStamp = timeStamp.split()[3]
    fulString = "Your next pill is "+medicineName+" at "+timeStamp[:-3]
    fulfillmentDict = {"fulfillmentText": fulString}
    print(fulfillmentDict, file=sys.stderr)
    return make_response(jsonify(fulfillmentDict))

