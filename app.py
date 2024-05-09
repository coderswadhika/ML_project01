from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
            raise HousingException(e, sys) from e
            logging.info(housing.error_message)
            logging.info("We are testing logging module")
    return "Starting Ml_project01"


if __name__=="__main__":
    app.run(debug=True)    