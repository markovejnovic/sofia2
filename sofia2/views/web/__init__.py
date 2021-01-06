# Sofia2 is a simple, easy-to-use, modular home automation system.
# Copyright (C) 2020 Marko Vejnovic
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from threading import Thread
from werkzeug.serving import make_server
from flask import Flask
from sofia2.views import View
from .api import DevicesResource

class ServerThread(Thread):
    """Creates a server on a separate thread."""

    def __init__(self, app):
        Thread.__init__(self)
        self.server = make_server('localhost', 5000, app)
        self.context = app.app_context()
        self.context.push()

    def run(self):
        self.server.serve_forever()

    def shutdown(self):
        self.server.shutdown()

class WebView(View):
    """Represents a WebView that sofia2 may use. This is a simple class which
    exposes the Flask server."""

    def __init__(self, device_manager):
        """Constructs the flask server."""
        super().__init__(device_manager)
        self.flask_app = Flask('sofia2')
        self.server = ServerThread(self.flask_app)

    def on_start(self):
        """Starts the Flask server."""
        self.server.start()

    def on_stop(self):
        self.server.shutdown()
