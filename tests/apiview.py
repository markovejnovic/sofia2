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

"""Contains the tests for the API view."""

import unittest
import json
import requests

class TestDevicesRoute(unittest.TestCase):
    """Tests whether the API view adheres to the API requirements."""

    def setUp():
        # TODO: Start the REST server
        pass

    def test_empty(self):
        """Tests whether the API correctly returns the information for 0
        devices."""
        mdata = json.loads(requests.get('http://localhost:8080/devices'))

        self.assertEqual(0, len(mdata))

    def test_one_device(self):
        """Tests whether the API correctly returns the information for one
        device."""
        class LedDevice(Device):
            def on_register(self):
                self.test_is_on = False

            def on_deregister(self):
                self.test_is_on = False

            def _set_state(self, state):
                self.test_is_on = state

            def get_handlers(self):
                return {
                    'TEMP_HIGH': [lambda msg: self._set_state(True)],
                    'TSENSE_ON': [lambda msg: self._set_state(False)]
                }
        self.led_device = LedDevice()
        self.device_manager.register_device(self.led_device)

        mdata = json.loads(requests.get('http://localhost:8080/devices'))
        self.assertEqual(1, len(mdata))
        self.assertEqual([
            {
                'name': 'LedDevice',
                'handlers': [ 'TEMP_SENSE', 'TSENSE_ON' ]
            }
        ], mdata)
