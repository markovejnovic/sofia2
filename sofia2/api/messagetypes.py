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

"""Contains Sofia's MessageType classes."""

import typing # pylint: disable=unused-import


class MessageType:
    """Base class for message types."""

    def __init__(self, name=None) -> None:
        """Represents a single message type.

        Parameters:
            name - The human-readable name of the message type.
        """
        self.name = name if name is not None else self.__class__.__name__


class DeviceMessageType(MessageType):
    """Base class for Device messagetypes."""

    def __init__(self, name=None):
        super().__init__(name)
