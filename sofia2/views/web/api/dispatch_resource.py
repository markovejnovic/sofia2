# Sofia2 is a simple, easy-to-use, modular home automation system.
# Copyright (C) 2020 Slobodanka Smilkova
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

"""Contains the DispatchResource REST resource."""

from flask_restful import Resource

class DispatchResource(Resource):
    """Handles the /dispatch route"""

    def __init__(self, device_manager):
        self.device_manager = device_manager

    def post(self, jsonMessage):
        """Sends a signal to sofia2.
	The jsonMessage should be a JSON type of the following form:

	{"type": "<text here>", "description": "<text here>", 
	"value": "<text here>"}

	"""
        self.device_manager.dispatch(jsonMessage, self)
        return '', 200 
