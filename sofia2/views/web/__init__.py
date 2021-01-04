from flask import Flask
from flask_restful import Resource, Api
from .api import DevicesResource

FLASK_SERVER = None

def get_web_server():
    """Either starts the currently running application or returns the already
    existing one."""
    # TODO: Make these objects
    global FLASK_SERVER
    if FLASK_SERVER is None:
        FLASK_SERVER = Flask('sofia2')
    return FLASK_SERVER

REST_API = None

def get_api_server():
    """Either starts the API server, or returns the already existing one if it
    exists."""
    # TODO: Make these objects
    global REST_API
    if REST_API is None:
        REST_API = Api(get_web_server())
        REST_API.add_resource(DevicesResource, '/devices')

    return REST_API
