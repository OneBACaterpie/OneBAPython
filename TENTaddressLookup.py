# Business Process:
# 1. A list of addresses is provided in an Excel file (MyTestAddressFile.xlsx). Require columns for "Street Address", "City", and "Zip Code".
# 2. Each address must be run through a lookup process to identify which legislative district they reside in, which results in a JSON formatted HTML page.

import json
from urllib.request import urlopen
from urllib.parse import quote

# ReturnLegislators() Returns Representative Name and Senator Name for an address. In this example, we'll be using a web page formatted as a JSON.

def ReturnLegislators():
  x = urlopen("https://www.mcgi.state.mi.us/ws_csstp/gis_services.svc/rest/geocodeAddress/?a=100%20N%20Capitol%20Ave%20Lansing%2048933&ma=false&tk=%7bTOKEN%7d").read()
  x = x.decode('utf-8')
  x = json.loads(x)
  RepName = x["geocodeAddressResult"][0]["MatchInfo"]["House"]["Name"]
  SenName = x["geocodeAddressResult"][0]["MatchInfo"]["Senate"]["Name"]
  
  print(f"Rep: {RepName}")
  print(f"Sen: {SenName}")

ReturnLegislators()

# Testing a custom URL function

def CustomURL():
  # Need to take an Address {Street Address, City, Zip Code} from an Excel file and create the custom URL
  Address = {"Street Address": "100 N Capitol Ave", "City": "Lansing", "Zip Code": "48933"}
  URLBeginning = "https://www.mcgi.state.mi.us/ws_csstp/gis_services.svc/rest/geocodeAddress/?a="
  URLMiddle = quote(Address["Street Address"] + " " + Address["City"] + " " + Address["Zip Code"])
  URLEnd = "&ma=false&tk=%7bTOKEN%7d"
  LookupURL = URLBeginning + URLMiddle + URLEnd
  print(LookupURL)
  x = urlopen(LookupURL).read()
  x = x.decode('utf-8')
  x = json.loads(x) 
  RepName = x["geocodeAddressResult"][0]["MatchInfo"]["House"]["Name"]
  SenName = x["geocodeAddressResult"][0]["MatchInfo"]["Senate"]["Name"]
  print(f"Rep: {RepName}")
  print(f"Sen: {SenName}")

CustomURL()
