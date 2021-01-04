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

"""The Sofia2 DeviceManager"""


class DeviceManager:
    """The DeviceManager controls each device as well as the communication
    between them. The DeviceManager also enables devices to be interfaced with
    through the ViewManager.
    """
    def __init__(self):
        self.devices = {}
        self.message_handlers = {}

    def register_device(self, device):
        """Registers a device with the DeviceManager, managing it and
        registering each message type that these devices can handle.
        """
        # Let us make sure that the device name is unique, before anything.
        try:
            self.devices[device.get_name()]
            raise DeviceExistsError()
        except KeyError:
            self.devices[device.get_name()] = None

        # First, let us store the device
        self.devices[device.get_name()] = device
        self.devices[device.get_name()].set_manager(self)

        # Secondly, call the on_register
        device.on_register()

        # Thirdly, store that device's handlers into the message_handlers.
        for k in device.get_handlers().keys():
            try:
                for handler in device.get_handlers()[k]:
                    self.message_handlers[k].append(handler)
            except KeyError:
                self.message_handlers[k] = device.get_handlers()[k]

    def get_all_devices(self):
        """Returns the list of all device objects."""
        # TODO: dict.values() is O(n), can be optimized if self.devices is not
        # a dict but a SQL database.
        return self.devices.values()

    def deregister_device(self, device):
        """Deregisters a device with the DeviceManager, removing its handlers.
        """
        # Remove the device from the list of devices.
        self.devices[device.get_name()] = None

    def dispatch(self, message, src):
        """Dispatches a message sent from a source through all devices which
        handle can handle a message.

        Example:
            dmgr.dispatch({
                'type': 'TEMP_SENSE',
                'description': 'The temperature is extremely high!',
                'value': 30
            }, self)
        """
        for handler in self.message_handlers[message['type']]:
            handler(message)
