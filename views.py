"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, request
from ABDS import app
from ABDS import assignRoute


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    deploy = assignRoute.assignRoute()
    deploying = deploy[0]
    sellingTicket = deploy[1]
    busCapacity = deploy[2]
    return render_template(
        'index.html',
        title='Automated Bus Distribution System',
        deploying=deploying,
        sellingTicket=sellingTicket,
        busCapacity=busCapacity,
        year=datetime.now().year,
    )

@app.route('/form')
def form():
    return render_template(
    'form.html',
    title='Automated Bus Distribution System',
    year=datetime.now().year,
    )


@app.route('/random')
def random():
    deploy = assignRoute.assignRoute()
    deploying = deploy[0]
    sellingTicket = deploy[1]
    busCapacity = deploy[2]
    return render_template(
        'index.html',
        title='Automated Bus Distribution System',
        deploying=deploying,
        sellingTicket=sellingTicket,
        busCapacity=busCapacity,
        year=datetime.now().year,
    )