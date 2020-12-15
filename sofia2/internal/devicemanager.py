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

        # Secondly, call the on_register
        device.on_register()

        # Thirdly, store that device's handlers into the message_handlers.
        for k in device.get_handlers().keys():
            if self.message_handlers[k] is None:
                self.message_handlers[k] = device.get_handlers()[k]
            else:
                for handler in device.get_handlers()[k]:
                    self.message_handlers[k].append(handler)

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
