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

# Built a new route for the precipitation analysis   
@app.route("/api/v1.0/precipitation")

# Next, we will create the precipitation() function.
# Add the line of code that calculates the date one year ago from the most recent date in the database.
# Write a query to get the date and precipitation for the previous year. 
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)  

# Built a new route for the stations analysis
@app.route("/api/v1.0/stations")

# With our route defined, we'll create a new function called stations()
# Create a query that will allow us to get all of the stations in our database.
# We want to start by unraveling our results into a one-dimensional array. 
    # To do this, we want to use the function np.ravel(), with results as our parameter.
    # Next, we will convert our unraveled results into a list. 
    # To convert the results to a list, we will need to use the list function, which is list(),
    # and then convert that array into a list. 
    # Then we'll jsonify the list and return it as JSON.
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Built a new route for temperature observations (tobs) for the previous year. 
@app.route("/api/v1.0/tobs")

# Create a function called temp_monthly() by adding the following code:
# Calculate the date one year ago from the last date in the database.
# unravel the results into a one-dimensional array and convert that array into a list. 
# Then jsonify the list and return our results.
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Built a new, and last, route for summary statistics report (minimum, average, and maximum temperatures).
# This route is, however, different from the previous ones in that we will have to provide 
# both a starting and ending date.
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Next, create a function called stats() to put our code in.
# Add parameters to our stats()function: a start parameter and an end parameter.
    # For now, set them both to None.
# Create a query to select the minimum, average, and maximum temperatures from our SQLite database. 
    # We'll start by just creating a list called sel.
# Since we need to determine the starting and ending date, add an if-not statement to our code. 
    # We'll need to query our database using the list that we just made. 
    # Then, we'll unravel the results into a one-dimensional array and convert them to a list. 
    # Finally, we will jsonify our results and return them.
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)


    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

