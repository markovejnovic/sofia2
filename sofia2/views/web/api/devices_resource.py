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

"""Contains the DevicesResource REST resource."""

from flask_restful import Resource

class DevicesResource(Resource):
    """Handles the /devices route"""

    def get(self):
        """Returns all of the devices that are known to sofia2."""
        # TODO: Implement.
        pass
