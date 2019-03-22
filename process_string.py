#!/usr/bin/python
import argparse
import sys
import unittest
import logging
import time

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

FREQ_OUT = {"day":60*60*24, "week":60*60*24*7, "hour":60*60}
FREQ_OUT.update({"hours":60*60, "days":60*60*24, "weeks":60*60*24*7})

def get_timestamps(string_raw, limit):
  FREQ_OUT = {"day":60*60*24, "week":60*60*24*7, "hour":60*60}
  FREQ_OUT.update({"hours":60*60, "days":60*60*24, "weeks":60*60*24*7})

  string = string_raw.replace(" a ", " every ")
  TIMESTAMP_LIMIT = int(limit)
  word_lst = [x.lower() for x in string.split()]
  EXT_INCR = 0.0
  INT_INCR = 1.0
  logger.debug(str(word_lst))

  if "every" in word_lst:
    logger.debug("Found EVERY")
    for index in range(len(word_lst)):
      word = word_lst[index]
      if word in FREQ_OUT:
	EXT_INCR = FREQ_OUT[word]
	logging.info("Set ext_incr: %d" % EXT_INCR)

    for index in range(len(word_lst)):
      word = word_lst[index]
      if word.isdigit():
	if word_lst[index+1] in ["time", "times"]:
  	  INT_INCR = int(word)
  	  logging.info("Set int_incr: %d" % INT_INCR)
	elif word_lst[index+1] in FREQ_OUT:
	  EXT_INCR *= int(word)
	  logging.info("Editted ext_incr: %d" % EXT_INCR)

  lcl = time.localtime()
  feed = [lcl[0], lcl[1], lcl[2], lcl[3], 0, 0, lcl[6], lcl[7], lcl[8]]
  base_time_sec = time.mktime(feed)
  times_lst = [base_time_sec]

  if EXT_INCR > 0:
    while len(times_lst) < TIMESTAMP_LIMIT:
      times_lst.append(times_lst[-1] + EXT_INCR/INT_INCR)

  return times_lst

  logging.debug("times_lst = " + str(times_lst))
  for time_val in times_lst:
    print time.asctime(time.localtime(time_val))

if __name__ == "__main__":
  main()
