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
