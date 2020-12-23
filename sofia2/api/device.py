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

"""This module exposes the Device ABC class used to interface with physical
or kernel-level devices."""

from abc import ABC, abstractmethod
from logging import getLogger
import typing # pylint: disable=unused-import

from ..internal.logging import handler as loghandler


class Device(ABC):
    """Represents a device which can be interacted with.

    The implemented devices may be actual physical devices, kernel-level
    devices or anything in between. Derive from this method.
    """

    def __init__(self) -> None:
        self.logger = getLogger(self.get_name())
        self.logger.addHandler(loghandler)
        self.manager = None

    def dispatch(self, message: dict) -> None:
        """Dispatches a message to the device manager. Use this function to
        notify either views or other devices.

        Each message dict that the dispatch takes must have the 'type' and
        'description' keys.
        """
        self.manager.dispatch(message, self)

    def on_register(self) -> None:
        """Called when the device is registered. Use this opportunity to reset
        your physical device, if necessary.
        """
        pass

    def on_deregister(self) -> None:
        """Called just before the device is deregistered. Use this to shut
        down the device, if necessary."""
        pass

    def get_handlers(self) -> dict:
        """This function should return a dictionary where each key is the
        op of a specific Message that this device can handle.

        This method is preferable to using handle_message as it avoids
        conditions and, in being declarative, is much easier to use.

        If a message is encountered which the returned dictionary contains, the
        DeviceManager will appropriately throw an exception.

        Eg. for an LED:
            def get_handlers(self):
                return {
                    'BLINK': [lambda msg: self._blink_led()],
                    'ON': [lambda msg: self._set_state(True)],
                    'OFF': [lambda msg: self._set_state(False)]
                }
        """
        return {}

    def get_name(self) -> str:
        """Returns the name of class. This can be overriden for custom names.
        By default returns the class name."""
        return self.__class__.__name__

    def set_manager(self, manager):
        """Sets the manager of this device. Internal use only."""
        self.manager = manager
