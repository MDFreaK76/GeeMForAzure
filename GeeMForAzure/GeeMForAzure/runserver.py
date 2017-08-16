"""
This script runs the GeeMForAzure application using a development server.
"""

from os import environ
from GeeMForAzure import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '443'))
    except ValueError:
        PORT = 443
    app.run(HOST, PORT)
