import os
import logging
from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

# Create Flask application
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)

# Enable Security Headers using Flask-Talisman
talisman = Talisman(
    app,
    content_security_policy={
        'default-src': '\'self\'',
        'object-src': '\'none\'',
    },
    force_https=False # Set to True in production
)

# Import the routes and models after app is created
from service import routes, models
from service.common import error_handlers

# Set up logging for production
print(f"Setting up logging hierarchy for {__name__}...")
