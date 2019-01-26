"""
I²C Module
==========

This module contains definitions for managing
and controlling I²C devices.
"""

import smbus2
import time


class I2CDevice:
    """
    This class represents an I²C device and implements it's 
    bare-metal functions like reading and writing bytes from 
    and to the device.

    The sleep at the end of every write method is necessary
    because of the clock speed of 100kHz every standard I²C
    device uses. By sleeping 0.0001 seconds after each write
    we make sure that we are not sending two bytes in one
    clock cycle.

    :ivar int addr: The address of the device on it's bus.
    :ivar int bus: The number of the bus the device is connected to.
    """

    def __init__(self, addr: int, bus: int):
        self.addr = addr
        self.bus = smbus2.SMBus(bus)

    def write_byte(self, byte: int):
        """
        Writes a byte to the device.

        :param int byte: The byte to write.
        """

        self.bus.write_byte(self.addr, byte)
        time.sleep(0.0001)

    def write_byte_register(self, register: int, byte: int):
        """
        Writes a byte to a specific register.

        :param int register: The address of the register to write to.
        :param int byte: The byte to write to the register.
        """

        self.bus.write_byte_data(self.addr, register, byte)
        time.sleep(0.0001)

    def write_block_register(self, register: int, block: int):
        """
        Writes a block of bytes to a specific register.

        :param int register: The address of the register to write to.
        :param int block: The block of bytes to write.
        """

        self.bus.write_i2c_block_data(self.addr, register, block)
        time.sleep(0.0001)

    def read_byte(self) -> int:
        """
        Reads a single byte from the device.

        :returns: The read byte.
        :rtype: int
        """

        return self.bus.read_byte(self.addr)

    def read_byte_register(self, register: int) -> int:
        """
        Reads a single byte from a specific register.

        :param int register: The address of the register to read from.

        :returns: The read byte.
        :rtype: int
        """

        return self.bus.read_byte_data(self.addr, register)

    def read_block_register(self, register: int, length: int) -> int:
        """
        Reads a block of bytes from a specific register.

        :param int register: The address of the register to read from.
        :param int length: The length of the block to read.

        :returns: The read block of bytes.
        :rtype: int
        """

        return self.bus.read_i2c_block_data(self.addr, register, length)


class I2CDisplay(I2CDevice):
    """
    This class represents an I²C enabled LCD display.
    It implements the I2CDevice and adds functions for
    printing text and toggling backlight. Displays with
    up to four lines are supported.

    :ivar int lines: The amount of lines on the display.
    :ivar int line_length: The line length of the display.
    :ivar bool backlight: The backlight status of the display, `True` means on, `False` means off. **Do not set this manually, use the functions for toggling backlight!**
    """

    ENABLE = 0b00000100
    """The enable bit."""
    READWRITE = 0b00000010
    """The read/write bit."""
    REGISTER = 0b00000001
    """The register selection bit."""

    def __init__(self, addr: int, bus: int, lines: int, line_length: int):
        I2CDevice.__init__(self, addr, bus)
        self.lines = lines
        self.line_length = line_length
        self.backlight = True
        self.setup()

    def setup(self):
        """
        Initializes the display by putting it into
        4-Bit mode, enabling backlight and clearing it.
        The sleep at the end is necessary to make sure the
        display fully initialized before doing anything else.

        **You don't have to call this manually, this function will
        automatically be called by the constructor.**
        """

        self.write(0x03)
        self.write(0x03)
        self.write(0x03)
        self.write(0x02)

        self.write(0x20 | 0x08 | 0x00 | 0x00)
        self.write(0x08 | 0x04)
        self.write(0x01)
        self.write(0x04 | 0x02)
        time.sleep(0.2)

    def strobe(self, byte: int):
        """
        Strobes a byte to the display.

        :param int byte: The byte to strobe.
        """

        if self.backlight:
            self.write_byte(byte | self.ENABLE | 0x08)
        else:
            self.write_byte(byte | self.ENABLE)
        time.sleep(0.0005)

        if self.backlight:
            self.write_byte((byte & ~self.ENABLE) | 0x08)
        else:
            self.write_byte(byte & ~self.ENABLE)
        time.sleep(0.0001)

    def write4(self, byte: int):
        """
        Writes a byte to the display in 4-Bit mode.

        :param int byte: The byte to write.
        """

        self.write_byte(byte | 0x08 if self.backlight else 0)
        self.strobe(byte)

    def write(self, byte, bit=0):
        """
        Writes a byte and control bit to the display.

        :param int byte: The byte to write.
        :param int bit: The control bit.
        """

        self.write4(bit | (byte & 0xF0))
        self.write4(bit | ((byte << 4) & 0xF0))

    def clear(self):
        """
        Clears the display.
        """

        self.write(0x01)

    def enable_backlight(self):
        """
        Enables the display backlight.
        """

        self.write_byte(0x08)
        self.backlight = True

    def disable_backlight(self):
        """
        Disables the display backlight.
        """

        self.write_byte(0x00)
        self.backlight = False

    def set_backlight(self, on: bool):
        """
        Sets the display backlight to the desired
        status, either on or off.

        :param bool on: The desired backlight status, *True* means on, *False* means off.
        """

        if type(on) is bool and on:
            self.enable_backlight()
        elif type(on) is bool and not on:
            self.disable_backlight()

    def print(self, string: str, line: int):
        """
        Prints a string to the given line. This
        method will not clear the remaining space
        on the line. 
        If *line* is greater than 4 or less than 1, 
        it will print to the first line.

        :param str string: The string to print.
        :param int line: The line to print to.
        """

        if line == 2:
            self.write(0xC0)
        elif line == 3:
            self.write(0x94)
        elif line == 4:
            self.write(0xD4)
        else:
            self.write(0x80)

        for char in string:
            self.write(ord(char), self.REGISTER)

    def print_center(self, string: str, line: int):
        """
        Prints a string centered in the given
        line. This function will, as it fills empty
        spaces with a space, overwrite all previous
        text on the line.
        If *line* is greater than 4 or less than 1, 
        it will print to the first line.

        :param str string: The string to print.
        :param int line: The line to print to.
        """

        string = string.center(self.line_length)
        self.print(string, line)

    def print_clear(self, string: str, line: int):
        """
        Prints a string to the given line,
        filling all remaining space with spaces.
        This way all previous text will be cleared.

        :param str string: The string to print.
        :param int line: The line to print to.
        """

        string = string.ljust(self.line_length - len(string))
        self.print(string, line)
