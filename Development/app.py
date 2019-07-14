import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, render_template, url_for, json, jsonify
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()

app = Flask(__name__)

#connection to My_SQL
engine = create_engine('mysql://root:root123@127.0.0.1:3306/stockml_db', pool_pre_ping=True)


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
cfg_profile = Base.classes.cfg_profile
ms_profile = Base.classes.ms_profile
cme_profile = Base.classes.cme_profile
jpm_profile = Base.classes.jpm_profile
gs_profile = Base.classes.gs_profile
pypl_profile = Base.classes.pypl_profile
brka_profile = Base.classes.brka_profile
brkb_profile = Base.classes.brkb_profile
usb_profile = Base.classes.usb_profile
ibkr_profile = Base.classes.ibkr_profile
axp_profile = Base.classes.axp_profile
stocks_profile = Base.classes.stocks_profile
yahoo_profiles = Base.classes.yahoo_profiles

# Create our session (link) from Python to the DB
session = Session(engine)

# ##################################################################
# ###################### Routes ###################################
# #################################################################

# function to create dictionary with all details on species
@app.route("/")
def index():
    """Return the Home page."""
    return render_template("index.html")

# Citizens_Financial_Group
# function to create dictionary with all details on species
@app.route("/Citizens_Financial_Group")
def Citizens_Financial_Group():
    """Return the Citizens_Financial_Group page."""
    return render_template("Citizens_Financial_Group.html")

# /MorganStanley
# function to create dictionary with all details on species
@app.route("/MorganStanley")
def MorganStanley():
    """Return the MorganStanley page."""
    return render_template("MorganStanley.html")

@app.route("/CMEGroup")
def CMEGroup():
    """Return the CMEGroup page."""
    return render_template("CMEGroup.html")
@app.route("/JPMorganChase")
def JPMorganChase():
    """Return the JPMorganChase page."""
    return render_template("JPMorganChase.html")

@app.route("/GoldmanSachsGroup")
def GoldmanSachsGroup():
    """Return the GoldmanSachsGroup page."""
    return render_template("GoldmanSachsGroup.html")

@app.route("/PayPalHoldings")
def PayPalHoldings():
    """Return the PayPalHoldings page."""
    return render_template("PayPalHoldings.html")

@app.route("/BerkshireHathawayA")
def BerkshireHathawayA():
    """Return the BerkshireHathawayA page."""
    return render_template("BerkshireHathawayA.html")

@app.route("/BerkshireHathawayB")
def BerkshireHathawayB():
    """Return the BerkshireHathawayB page."""
    return render_template("BerkshireHathawayB.html")

@app.route("/USBancorp")
def USBancorp():
    """Return the USBancorp page."""
    return render_template("USBancorp.html")

@app.route("/InteractiveBrokers")
def InteractiveBrokers():
    """Return the InteractiveBrokers page."""
    return render_template("InteractiveBrokers.html")

@app.route("/AmericanExpress")
def AmericanExpress():
    """Return the AmericanExpress page."""
    return render_template("AmericanExpress.html")

@app.route("/charts")
def charts():
    """Return the charts page."""
    return render_template("charts.html")

@app.route("/tables")
def tables():
    """Return the tables page."""
    return render_template("tables.html")

@app.route("/heatmap")
def heatmap():
    """Return the heatmap page."""
    return render_template("heatmap.html")

def get_data_stockdetails(selected_stock):

    sel=[stocks_profile.dates,
        stocks_profile.open,
        stocks_profile.high,
        stocks_profile.low,
        stocks_profile.close,
        stocks_profile.adjusted_close,
        stocks_profile.volume,
        stocks_profile.ticker,
        yahoo_profiles.Ticker,
        yahoo_profiles.Description,
        yahoo_profiles.Company_Name]

    results = session.query(*sel).\
            filter(stocks_profile.ticker == yahoo_profiles.Ticker).all() 
    return results

    
    print(results)

   

if __name__ == '__main__':
    app.run(debug=True)