"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.config["DEBUG"] = True

import ABDS.views

