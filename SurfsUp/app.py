# Import the dependencies.

import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy 
import flask
from flask import Flask , jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session


#################################################
# Database Setup
#################################################

# reflect an existing database into a new model

engine = create_engine("sqlite:///../Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(autoload_with=engine)

# reflect the tables
# Save references to each table
# Create our session (link) from Python to the DB

measurements = Base.classes.measurement
stations = Base.classes.station
session = Session(engine)





#################################################
# Flask Setup
#################################################

app = Flask(__name__)

@app.route("/")
def index():
    return(f"Welcome! Find data about Hawaii's stations and their temperature readings. Here are the available routes:<br/>"
           f"/api/v1.0/precipitation<br/>"
           f"/api/v1.0/stations<br/>"
           f"/api/v1.0/tobs<br/>"
           f"Enter a start date at the end of the following URL to find min, max, and average temps!<br/>"
           f"/api/v1.0/<start><br/>"
           f"Enter a start and end date before/after the last slash to find min, max, and average temps!<br/>"
           f"/api/v1.0/<start>/<end><br/>"
          )



#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/precipitation")
def precipitation():
    precip_data = session.query(measurements.date,measurements.prcp).\
    filter(measurements.date >= '2016-08-23').\
    order_by(measurements.date).all()
    precip_dict = {date : x for date , x in precip_data}
    return jsonify(precip_dict)

@app.route("/api/v1.0/stations")
def station():
    result = session.query(stations.station).all()
    stations_list = list(np.ravel(result))
    return jsonify (stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    active_temps = session.query(measurements.tobs).filter(measurements.date >= '2016-08-18').\
                   filter(measurements.station == 'USC00519281').all()
    tobs_route = list(np.ravel(active_temps))
    return jsonify(tobs_route)
    
@app.route("/api/v1.0/<start>")

def start_date(start):
    temps = session.query(func.min(measurements.tobs),func.max(measurements.tobs),func.avg(measurements.tobs).\
    filter(measurements.date >= start)).all()
    start_route = list(np.ravel(temps))
    return jsonify(start_route)

@app.route("/api/v1.0/<start>/<end>")
def start_end_route(start,end):
    specific_range_temps= session.query(func.min(measurements.tobs),func.max(measurements.tobs),func.avg(measurements.tobs).\
    filter(measurements.date >= start).\
    filter(measurements.date <= end)).all()
    specific_range_ravel = list(np.ravel(specific_range_temps))
    return jsonify(specific_range_ravel)
    
    
if __name__=="__main__":
    app.run(debug=True)
