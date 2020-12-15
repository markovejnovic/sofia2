"""Sets up the logging Sofia2 uses."""

from logging import Formatter, StreamHandler


handler = StreamHandler()

formatter = Formatter('%(asctime)s :: %(name)s [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
