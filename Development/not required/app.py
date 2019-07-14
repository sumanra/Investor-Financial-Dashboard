import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+mysqlconnector://root:root123@127.0.0.1:3306/stockml_db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/apple")
def index():
    """Return the Apple page."""
    return render_template("apple.html")

@app.route("/tables")
def index():
    # Use Pandas to perform the sql query
    pd.read_sql_query('select * from mcd_Stock', con=engine)
    """Return the tables page."""
    return render_template("tables.html")

@app.route("/charts")
def index():
    """Return the charts page."""
    return render_template("charts.html")

@app.route("/names")
def names():
    """Return a list of sample names."""

    # # Use Pandas to perform the sql query
    # stmt = db.session.query(stocks_profile).statement
    # df = pd.read_sql_query(stmt, db.session.bind)
    #connection to My_SQL
    engine = create_engine('mysql://root:root123@127.0.0.1:3306/stockml_db', pool_pre_ping=True)


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

    # Return a list of the column names (sample names)
    return jsonify(list(df.columns)[2:])


@app.route("/metadata/<sample>")
def sample_metadata(sample):
    """Return the MetaData for a given sample."""
    sel = [
        stocks_profile.dates,
        stocks_profile.open,
        stocks_profile.high,
        stocks_profile.low,
        stocks_profile.close,
        stocks_profile.adjusted_close,
        stocks_profile.volume,
        stocks_profile.ticker,
        yahoo_profiles.Ticker,
        yahoo_profiles.Description,
        yahoo_profiles.Company_Name
    ]

    results = db.session.query(*sel).filter(Samples_Metadata.sample == sample).all()

    # Create a dictionary entry for each row of metadata information
    sample_metadata = {}
    for result in results:
        sample_metadata["sample"] = result[0]
        sample_metadata["ETHNICITY"] = result[1]
        sample_metadata["GENDER"] = result[2]
        sample_metadata["AGE"] = result[3]
        sample_metadata["LOCATION"] = result[4]
        sample_metadata["BBTYPE"] = result[5]
        sample_metadata["WFREQ"] = result[6]

    print(sample_metadata)
    return jsonify(sample_metadata)


@app.route("/samples/<sample>")
def samples(sample):
    """Return `otu_ids`, `otu_labels`,and `sample_values`."""
    stmt = db.session.query(Samples).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    # Filter the data based on the sample number and
    # only keep rows with values above 1
    sample_data = df.loc[df[sample] > 1, ["otu_id", "otu_label", sample]]
    # Format the data to send as json
    data = {
        "otu_ids": sample_data.otu_id.values.tolist(),
        "sample_values": sample_data[sample].values.tolist(),
        "otu_labels": sample_data.otu_label.tolist(),
    }
    return jsonify(data)


if __name__ == "__main__":
    app.run()
