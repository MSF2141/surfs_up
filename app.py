# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

# Import dependencies for SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import dependencies for Flask
from flask import Flask, jsonify

# Set up the database
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save the references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database with the following code:
session = Session(engine)

# Create the Flask app
app = Flask(__name__)

# Define the welcome route using the code below:
# Next, add the precipitation, stations, tobs, and temp routes that we'll need for this module 
# into our return statement. We'll use f-strings to display them for our investors:
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
    
