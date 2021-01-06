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

"""This module contains the base class used in making views. Note that each
view that is used will be a singleton."""

from sofia2.utils import Singleton
from sofia2.internal import DeviceManager

class View:
    """Represents the base class for any view that sofia2 may have."""

    def __init__(self, device_manager):
        self.device_manager = device_manager

    def get_dmanager(self):
        """Returns the sofia2 device manager. Used for convenience."""
        return self.device_manager

    def get_devices(self):
        """Convenience function which returns all devices that are currently
        registered."""
        return self.device_manager.get_all_devices()

    def on_start(self):
        """An overridable method that is called when sofia2 starts this view.
        """
