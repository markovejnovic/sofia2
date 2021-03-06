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

"""Tests the DeviceManager"""

import unittest
from threading import Thread

from sofia2.api import Device
from sofia2.internal import DeviceManager


class TestDeviceManager(unittest.TestCase):
    """Tests the DeviceManager can successfuly be created."""

    def setUp(self):
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

        class AlarmDevice(Device):
            def on_register(self):
                self.test_is_beeping = False

            def on_deregister(self):
                self.test_is_beeping = False

            def _beep(self, state):
                self.test_is_beeping = state

            def get_handlers(self):
                return {
                    'TEMP_LOW': [lambda msg: self._beep(False)],
                    'TEMP_HIGH': [lambda msg: self._beep(True)]
                }

        class TempSensor(Device):
            def on_register(self):
                self.test_temp = 30
                self._thread = Thread(target=self._read_temp)
                self._thread.start()

            def _read_temp(self):
                self.test_temp = 40 # Read temp

                # Dispatch messages around
                self.dispatch({
                    'type': 'TEMP_HIGH',
                    'description': 'The temp is critical.',
                    'value': self.test_temp
                })

                self.test_temp = 30

                self.dispatch({
                    'type': 'TEMP_LOW',
                    'description': 'The temp is nominal.',
                    'value': self.test_temp
                })

        self.alarm_device = AlarmDevice()
        self.led_device = LedDevice()
        self.temp_sensor = TempSensor()

        self.device_manager = DeviceManager()
        self.device_manager.register_device(self.alarm_device)
        self.device_manager.register_device(self.led_device)

    def test_add_temp_sensor(self):
        self.device_manager.register_device(self.temp_sensor)
        self.assertTrue(self.led_device.test_is_on)

    def test_get_all_devices(self):
        self.assertEqual(2, len(self.device_manager.get_all_devices()))
        self.assertIn(self.alarm_device, self.device_manager.get_all_devices())
        self.assertIn(self.led_device, self.device_manager.get_all_devices())
