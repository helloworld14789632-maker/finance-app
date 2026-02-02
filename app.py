"""
Entry point for Flask application.
This file enables Gunicorn to run the app with: gunicorn app:app
"""
# Import the Flask app instance from the app package
# This is the entry point for both development and production
from app import app  # noqa: F401

if __name__ == '__main__':
    app.run(debug=True)
