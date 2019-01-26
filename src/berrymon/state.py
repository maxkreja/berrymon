"""
State Module
============

Contains definitions for managing the state and
data of the Berrymon app.
"""

from .config import Config
from .i2c import I2CDisplay
from . import sysinfo


class State:
    """
    This class represents a sate object for the Berrymon application.
    The state describes the current data and has functions 
    to modify and update itself.

    :ivar Config config: The current configuration.
    :ivar str username: The current username.
    :ivar float load: The current CPU load in percent.
    :ivar float temp: The current CPU temperature in degree celsius.
    :ivar str ip: The current IP address.
    :ivar I2CDisplay display: A display that can be added to the state optionally.
    """

    def __init__(self, config_path: str):
        self.config = Config()
        self.config.load_from_file(config_path)

        self.username = ""
        self.load = 0.0
        self.temp = -5.0
        self.ip = "UNKOWN"
        self.display = None

    def update(self):
        """
        Updates the state variables.
        """

        self.username = sysinfo.get_username()
        self.load = sysinfo.get_cpu_load()
        self.temp = sysinfo.get_cpu_temp()
        self.ip = sysinfo.get_ip()

    def add_display(self, display: I2CDisplay):
        """
        Adds a display to the state.

        :param I2CDisplay display: The display to add.
        """
        self.display = display
