
# Dependencies Setup


import datetime as dt


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# Database Setup


# --- create engine using the `hawaii.sqlite` database file ---
engine = create_engine('sqlite:///Resources/hawaii.sqlite')

# --- reflect an existing database into a new model ---
Base = automap_base()

# --- reflect the tables ---
Base.prepare(engine, reflect=True)

# --- save references to the tables ---
measurement = Base.classes.measurement
station = Base.classes.station


# Flask Setup


# --- create an instance of the Flask class ---
app = Flask(__name__)


# --- Flask Routes ---


