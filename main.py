#!/usr/bin/env python3

import os
from os.path import join, dirname
from dotenv import load_dotenv


# load the .env file into local environment variables
load_dotenv(join(dirname(__file__), ".env"))


# populate the variables with the environment variable values
ip = os.getenv("IP")
port = os.getenv("PORT")

