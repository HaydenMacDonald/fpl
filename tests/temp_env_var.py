import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.abspath("credentials.cfg"))

TEMP_ENV_VARS = {
    "FPL_EMAIL": config["CREDENTIALS"]["FPL_EMAIL"],
    "FPL_PASSWORD": config["CREDENTIALS"]["FPL_PASSWORD"]
}

ENV_VARS_TO_SUSPEND = [
]
