import argparse
import requests
import logging
import time, random, sys, json
import process_string as timestamps

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
  json_data = requests.get("https://stonehill-hackathon.firebaseio.com/.json").text
  json_dict = json.loads(json_data)

  parser = argparse.ArgumentParser()
  parser.add_argument("-t", "--test", action="store_true", help="Test version")
  parser.add_argument("-p", "--prescription", help="Enter the prescription you want to test")
  parser.add_argument("-l", "--limit", help="How many timestamps?")
  args = vars(parser.parse_args())
  logger.debug(args["prescription"])

  if args["test"]:
    json_dict.update({"prescription":str(args["prescription"])})

  return timestamps.get_timestamps(json_dict["prescription"], args["limit"])

if __name__ == "__main__":
  print main()
