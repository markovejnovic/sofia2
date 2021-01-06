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
from multiprocessing import Process
import requests
from sofia2.api.device import Device
from sofia2.internal.devicemanager import DeviceManager
from sofia2.views.web.api.dispatch_resource import DispatchResource
from sofia2.views.web import WebView
from sofia2.views.web.api import RESTView

class TestDevicesRoute(unittest.TestCase):
    """Tests whether the API view adheres to the API requirements."""

    def setUp(self):
        """Tests whether the API correctly returns the information for one
        device."""

        # Let's create a dummy LED device
        class LedDevice(Device):
            """Dummy LED Device"""

            def __init__(self):
                super().__init__()
                self.test_is_on = False

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

        # Convenience. URL we will be testing
        self.base_url = 'http://localhost:5000/devices'

        # Let's first create an LED device
        self.led_device = LedDevice()

        # Let's create the device manager and register our device object
        self.device_manager = DeviceManager()
        self.device_manager.register_device(self.led_device)

        # Create our WebView (required for RESTView), then RESTView.
        self.wview = WebView(self.device_manager)
        self.rview = RESTView(self.device_manager, self.wview.flask_server)

        # Used for debugging purposes, disables flask's auto-reload feature on
        # code change.
        self.wview.flask_server.use_reloader = False

        # We actually want the server to start on another process. If we were
        # starting on the same process as the one we are running, then we would
        # never actually continue on from this test, as flask would start
        # taking control of the instruction pointer. This way it starts on its
        # own process and we can continue.
        self.flask_proc = Process(target=self.wview.on_start)
        self.flask_proc.start() # Start that server

    def tearDown(self):
        # After each test is done we want to stop the process.
        self.flask_proc.terminate()

    def test_length_is_one(self):
        """Asserts that the number of devices is 1"""
        # Let's fetch from localhost/devices and convert that into json
        mdata = requests.get(self.base_url).json()

        # Assert the length of that is 1 (because we registered one device)
        self.assertEqual(1, len(mdata))

    def test_values_are_correct(self):
        """Asserts that the values are as expected."""
        # Let's fetch from localhost/devices and convert that into json
        mdata = requests.get(self.base_url).json()

        # Assert the values are as we expected.
        self.assertEqual([
            {
                'name': 'LedDevice',
                'handlers': [ 'TEMP_HIGH', 'TSENSE_ON' ]
            }
        ], mdata)

class TestDispatchRoute(unittest.TestCase):
    """Tests whether the API view adheres to the API requirements."""

    def setUp(self):
        """Tests whether the API correctly returns the posted signal
	to the device manager."""

        # URL we will be testing
        self.base_url = 'http://localhost:5000/dispatch'

        # Let's create the device manager
        self.device_manager = DeviceManager()

	# We send a signal to the device manager
        requests.post(self.base_url, data={"type": "TEMP_SENSE", 
        "description": "The temperature is extremely high!", "value": 33})

        # Create our WebView (required for RESTView), then RESTView.
        self.wview = WebView(self.device_manager)
        self.rview = RESTView(self.device_manager, self.wview.flask_server)

        # Used for debugging purposes, disables flask's auto-reload feature on
        # code change.
        self.wview.flask_server.use_reloader = False

        # Server starts on another process
        self.flask_proc = Process(target=self.wview.on_start)
        self.flask_proc.start() # Start that server

    def tearDown(self):
        # After each test is done we want to stop the process.
        self.flask_proc.terminate()

    def test_values_are_correct(self):
        # Fetch from localhost/dispatch and convert that into json
        mdata = requests.get(self.base_url).json()

        # Assert the values are as we expected.
        self.assertEqual([
            {
                'type': 'TEMP_SENSE',
                'description': 'The temperature is extremely high!',
                'value': 33
            }
        ], mdata)


if __name__ == "__main__":
    unittest.main()
