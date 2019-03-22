import argparse
import requests
import time, random, sys, json
from firebase import firebase
fb = firebase.FirebaseApplication("https://stonehill-hackathon.firebaseio.com/")

FREQ_OUT = {"day":60*60*24, "week":60*60*24*7, "hour":60*60}
FREQ_OUT.update({"hours":60*60, "days":60*60*24, "weeks":60*60*24*7})
MATCH = [["once","1 time"], ["twice","2 times"], ["thrice","3 times"]]

def get_timestamps(string_raw, limit):
  FREQ_OUT = {"day":60*60*24, "week":60*60*24*7, "hour":60*60}
  FREQ_OUT.update({"hours":60*60, "days":60*60*24, "weeks":60*60*24*7})

  string = string_raw.replace(" a ", " every ")
  for (x, y) in MATCH:
    string = string.replace(x, y)
  TIMESTAMP_LIMIT = int(limit)
  word_lst = [x.lower() for x in string.split()]
  EXT_INCR = 0.0
  INT_INCR = 1.0

  if "every" in word_lst:
    for index in range(len(word_lst)):
      word = word_lst[index]
      if word in FREQ_OUT:
        EXT_INCR = FREQ_OUT[word]

    for index in range(len(word_lst)):
      word = word_lst[index]
      if word.isdigit():
        if word_lst[index+1] in ["time", "times"]:
          INT_INCR = int(word)
        elif word_lst[index+1] in FREQ_OUT:
          EXT_INCR *= int(word)

  lcl = time.localtime()
  if lcl[4] == 59:
    lcl[4] = -1
    lcl[3] += 1
  feed = (lcl[0], lcl[1], lcl[2], lcl[3], lcl[4]+1, 0, lcl[6], lcl[7], lcl[8])
  base_time_sec = time.mktime(feed)
  times_lst = [base_time_sec]

  if EXT_INCR > 0:
    while len(times_lst) < TIMESTAMP_LIMIT:
      times_lst.append(times_lst[-1] + EXT_INCR/INT_INCR)

  return times_lst

  for time_val in times_lst:
    print (time.asctime(time.localtime(time_val)))

def recursion(prescr, prescr_lst, in_prescr, ts_dict, idx):
  if idx >= len(prescr_lst) - 1:
    return ts_dict

  ts_dict[prescr_lst[idx]] = ""
  count = idx + 1
  while count < len(prescr_lst) and prescr_lst[count] not in in_prescr:
    ts_dict[prescr_lst[idx]] += prescr_lst[count] + " "
    count += 1

  #print ts_dict
  return recursion(prescr, prescr_lst, in_prescr, ts_dict, count)

def main():
  json_data = requests.get("https://stonehill-hackathon.firebaseio.com/.json").text
  json_dict = json.loads(json_data)
  med_db = json_dict["medicalDatabase"]
  med_lst = med_db.keys()
  prescr = json_dict["prescription"]
  in_prescr = []
  med_match_lst = []
  ts_dict = {}
  #print med_lst, prescr

  for medic in med_lst:
    if medic in prescr:
      in_prescr.append(medic.replace(" ",""))
    prescr = prescr.replace(medic, medic.replace(" ", ""))
    med_match_lst.append(medic.replace(" ", ""))

  #print prescr, in_prescr
  prescr_lst = prescr.split()
  idx = 0
  while idx < len(prescr_lst) and prescr_lst[idx] not in in_prescr:
    idx += 1

  fn_dict = recursion(prescr, prescr_lst, in_prescr, ts_dict, idx)
  #return fn_dict, in_prescr

  to_jsonify = {}
  for medic in in_prescr:
    to_jsonify.update({medic:get_timestamps(fn_dict[medic], 20)})

  upload_val = json.dumps(to_jsonify)
  fb.put("", "timestamps", upload_val)

if __name__ == "__main__":
  print (main())
