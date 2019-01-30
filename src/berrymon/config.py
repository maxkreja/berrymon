"""
Config Module
=============

This module contains definitions for
the configuration of Berrymon.
"""

import json


class Config:
    """
    This class represents a configuration for Berrymon with 
    information like the API host address or the address of 
    an LCD display that’s meant to be used by Berrymon.

    :ivar str host: The API host address.
    :ivar int port: The API port.
    :ivar bool enable_lcd: Determines if an LCD display should be used or not.
    :ivar lcd_address: The address of a connected display.
    :ivar lcd_bus: The bus number of a display is connected to.
    :ivar lcd_lines: The amount of lines on a connected display.
    :ivar lcd_line_length: The line length of a connected display.
    """

    def __init__(self):
        self.host = "0.0.0.0"
        self.port = 2374
        self.enable_lcd = False
        self.lcd_addr = 0x27
        self.lcd_bus = 1
        self.lcd_lines = 2
        self.lcd_line_length = 16

    def load_from_file(self, path: str):
        """
        Loads configuration values from 
        a JSON file specified by the *path*.

        :param str path: The path of the JSON configuration file.
        """

        contents = json.load(open(path))
        self.host = str(contents["host"])
        self.port = int(contents["port"])
        self.enable_lcd = contents["enable_lcd"]
        self.lcd_addr = int(contents["lcd_addr"], 16)
        self.lcd_bus = int(contents["lcd_bus"])
        self.lcd_lines = int(contents["lcd_lines"])
        self.lcd_line_length = int(contents["lcd_line_length"])

    def save_to_file(self, path: str):
        """
        Saves the current configuration to a
        JSON file specified by the *path*

        :param str path: The path of the JSON configuration file.
        """

        json.dump({"host": self.host,
                   "port": self.port,
                   "enable_lcd": self.enable_lcd,
                   "lcd_addr": hex(self.lcd_addr),
                   "lcd_bus": self.lcd_bus,
                   "lcd_lines": self.lcd_lines,
                   "lcd_line_length": self.lcd_line_length}, open(path))
