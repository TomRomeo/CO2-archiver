#!/usr/bin/env python3

import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests


# load the .env file into local environment variables
load_dotenv(join(dirname(__file__), ".env"))


# populate the variables with the environment variable values
protocoll = os.getenv("PROTOCOLL")
ip = os.getenv("IP")
port = os.getenv("PORT")
db = os.getenv("DB")
parameters = os.getenv("PARAMETERS")


# aquire the data
# dummy data for now


value = "0.1"

# push the data to the remote server

url = protocoll+ip+":"+port+"/write?db="+db
datastring = "c02,"+parameters+",value="+value

r = requests.post(url, data=datastring)
if not (r.ok()):
    print("Something went wrong while trying to send the data to the server")
    print(r.status_code)
    print(r.json())
