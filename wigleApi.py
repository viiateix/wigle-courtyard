#!/usr/bin/python
#
# Custom Wigle API
# ----------------
# Queries the wigle.net database. Current uses include:
# - Obtain list of observed ESSIDs within defined search box, all date ranges.
# - 
#
# Note that Wigle's API is neither fully documented nor stable. This code will
# likely require regular revision and update.
#
# Requires:
# - Wigle account for API "Name" and "Token" credentials

import requests

######################
# USER-EDITED VALUES #
######################

BOX = {
    "NORTH": 48.351312, 
    "SOUTH": 46.645242,
    "EAST": -121.253449,
    "WEST": -123.713599
    }

API_NAME  = "AIDf798675efa87a7c2759dbf84dc3ba06a"
API_TOKEN = "0f0ba634b0f21f1de853fdb5124f5464"

BASE_URL = "https://api.wigle.net"

def getEssidSearch(ssid):
  query_url = BASE_URL + "/api/v2/network/search"
  params = "ssid=" + ssid
  print params
  r = requests.get(query_url, params, auth=(API_NAME, API_TOKEN))
  print r.status_code
  print r.json()

if __name__ == "__main__":
  ssid = raw_input("Enter the SSID. > ")
  getEssidSearch(ssid)
  exit(0)

