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
  "ACCT_NAME": "g3td0wn",
  "API_NAME" : "AIDf798675efa87a7c2759dbf84dc3ba06a",
  "API_TOKEN": "0f0ba634b0f21f1de853fdb5124f5464"})

API_STORE.append({
  "ACCT_NAME": "goomba9999",
  "API_NAME" : "AID22f090044d761cd0d893803260f5c662",
  "API_TOKEN": "e1c16b46a617da81abde11e17e79e397"})

API_STORE.append({
  "ACCT_NAME": "goomba1000",
  "API_NAME" : "AIDf0fe4d405d0961039c846a44d7b01cf1",
  "API_TOKEN": "3b14c4abed67866778b65a9a3e25b265"})

API_STORE.append({
  "ACCT_NAME": "goomba1001",
  "API_NAME" : "AID1d1b6e1fed5ba4ce93a5f0bf48f56f10",
  "API_TOKEN": "b4cfcd378cd1659bad702a02be0187ca"})

API_STORE.append({
  "ACCT_NAME": "goomba1002",
  "API_NAME" : "AIDdb4394425065702036e67f8eb66e76ac",
  "API_TOKEN": "c8342e23d7c61aa2b437c5c9e53af540"})




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
  choice = raw_input("[>] Select the account to use (0 thru " + str(len(API_STORE)-1)"

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

