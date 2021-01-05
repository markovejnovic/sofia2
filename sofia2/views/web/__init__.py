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

from flask import Flask
from sofia2.views import View
from .api import DevicesResource

class WebView(View):
    """Represents a WebView that sofia2 may use. This is a simple class which
    exposes the Flask server."""

    def __init__(self, device_manager):
        """Constructs the flask server."""
        super().__init__(device_manager)
        self.flask_server = Flask('sofia2')

    def on_start(self):
        """Starts the Flask server."""
        self.flask_server.run()
