# Business Process:
# 1. A list of addresses is provided in an Excel file (MyTestAddressFile.xlsx). Require columns for "Street Address", "City", and "Zip Code".
# 2. Each address must be run through a lookup process to identify which legislative district they reside in, which results in a JSON formatted HTML page.

import json
from urllib.request import urlopen
import pandas as pd

# ReturnLegislators() Returns Representative Name and Senator Name from JSON. In this example, we'll be using a web page formatted as a JSON.

def ReturnLegislators():
  x = urlopen("https://www.mcgi.state.mi.us/ws_csstp/gis_services.svc/rest/geocodeAddress/?a=100%20N%20Capitol%20Ave%20Lansing%2048933&ma=false&tk=%7bTOKEN%7d")
  addressInfo = json.loads()
  RepName = addressInfo(['geocodeAddressResult']['MatchInfo']['House']['Name']
  SenName = addressInfo(['geocodeAddressResult']['MatchInfo']['Senate']['Name']
  print(f"Rep: {RepName}")
  print(f"Sen: {SenName}")

ReturnLegislators()
