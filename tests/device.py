"""Tests the Device ABC."""

import unittest
from sofia2.api import Device


class TestCustomDevice(unittest.TestCase):
    """Tests whether a custom device can successfuly be created."""

    def setUp(self):
        class MDevice(Device):
            def __init__(self):
                super().__init__()
                self.registered = False
                self.deregistered = False
                self.led = False

            def on_register(self):
                self.registered = True

            def on_deregister(self):
                self.deregistered = True

            def get_name(self):
                return 'My Device'

            def _turn_on_led(self):
                # Call the appropriate funcs
                self.led = True

            def get_handlers(self):
                return {
                    'LED_ON': [lambda msg: self._turn_on_led()]
                }

        self.mdevice = MDevice()

    def test_name(self):
        self.assertEqual('My Device', self.mdevice.get_name())

    def test_on_register(self):
        self.mdevice.on_register()
        self.assertTrue(self.mdevice.registered)

    def test_on_deregister(self):
        self.mdevice.on_deregister()
        self.assertTrue(self.mdevice.deregistered)

    def test_get_handlers(self):
        self.mdevice.get_handlers()['LED_ON'][0]({})
        self.assertTrue(self.mdevice.led)


class TestMinimalCustoMDevice(unittest.TestCase):
    """Tests whether a minimal custom device can successfuly be created."""

    def setUp(self):
        class MDevice(Device):
            def __init__(self):
                super().__init__()
                self.registered = False
                self.deregistered = False
                self.led = False

            def on_register(self):
                self.registered = True

            def on_deregister(self):
                self.deregistered = True

            def _blink_led(self):
                self.led = True

            def get_handlers(self):
                return {
                    'LED_ON': [lambda msg: self._blink_led()]
                }

        self.mdevice = MDevice()

    def test_name(self):
        self.assertEqual('MDevice', self.mdevice.get_name())

    def test_on_register(self):
        self.mdevice.on_register()
        self.assertTrue(self.mdevice.registered)

    def test_on_deregister(self):
        self.mdevice.on_deregister()
        self.assertTrue(self.mdevice.deregistered)

    def test_get_handlers(self):
        self.mdevice.get_handlers()['LED_ON'][0]({})
        self.assertTrue(self.mdevice.led)
