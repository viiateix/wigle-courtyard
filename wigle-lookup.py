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

# Store all the Wigle accounts and API keys
# Format for each additional API key set:
#
# API_STORE.append({
#  "ACCT_NAME":"XXXXXXXXXXXXXX",
#  "API_NAME" :"XXXXXXXXXXXXXX", 
#  "API_TOKEN":"XXXXXXXXXXXXXX"})

API_STORE = []

API_STORE.append({
  "ACCT_NAME": "Put account username here in quotes",
  "API_NAME" : "HASHhashHASHhashHASHhash",
  "API_TOKEN": "HASHhashHASHhashHASHhash"})




####################
#      SCRIPT      #
####################

BASE_URL = "https://api.wigle.net"

def printApiStore():
  print "[*] Available API creds"
  print "    -------------------"
  for ii in range(0,len(API_STORE)):
    print "[" + str(ii) + "] " + "Account: " + API_STORE[ii]["ACCT_NAME"]
    print "    API Name: " + API_STORE[ii]["API_NAME"]
    print "    API Token: " + API_STORE[ii]["API_TOKEN"]
    print
  return

def chooseApiCreds():
  choice = raw_input("[>] Select the account to use (0 thru " + str(len(API_STORE)-1) + ") ")

def getEssidSearch(ssid):
  query_url = BASE_URL + "/api/v2/network/search"
  params = "ssid=" + ssid
  print params
  r = requests.get(query_url, params, auth=(API_NAME, API_TOKEN))
  print r.status_code
  print r.json()

if __name__ == "__main__":
  printApiStore()
  chosenApiCreds = chooseApiCreds()
  print API_STORE[0]["ACCT_NAME"]
  print API_STORE[0]["API_NAME"]
  print API_STORE[0]["API_TOKEN"]
  print
  for creds in API_STORE:
    print "ACCT_NAME = " + creds["ACCT_NAME"]
    print "API_NAME = " + creds["API_NAME"]
    print "API_TOKEN = " + creds["API_TOKEN"]
    print
  exit(0)
  ssid = raw_input("Enter the SSID. > ")
  getEssidSearch(ssid)
  exit(0)

