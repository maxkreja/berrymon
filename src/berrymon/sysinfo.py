"""
Sysinfo Module
==============

This module contains functions for
accessing information about the system
like CPU usage or temperature.
"""

import os
import pwd
import psutil
import subprocess


def get_username() -> str:
    """
    Returns the username of the user that
    is running the Berrymon process.

    :returns: The username of the current user.
    :rtype: str
    """

    return pwd.getpwuid(os.getuid())[0]


def get_cpu_load(format=False) -> float:
    """
    Returns the current system CPU load in
    percent as floating point number.

    :returns: The system's CPU load in percent.
    :rtype: float
    """

    return psutil.cpu_percent()


def get_cpu_temp() -> float:
    """
    Returns the CPU temperature in Celsius as
    floating point number.

    **This function will only work on the Raspberry Pi platform
    and therefore returns -5 if it's not executed on a Raspberry Pi.**

    :returns: The CPU temperature in percent.
    :rtype: float
    """

    try:
        return float(open("/sys/class/thermal/thermal_zone0/temp").read()) / 1000
    except:
        return -5.0


def get_ip() -> str:
    """
    Returns the first of the external IP addresses that are
    returned by the Linux system command "hostname -I". 
    If the system is not connected to any network, 'UNKOWN' will 
    be returned.

    :returns: The external IP address system.
    :rtype: str
    """

    output = subprocess.run(["hostname", "-I"], stdout=subprocess.PIPE).stdout
    output = output.decode("utf-8").strip().split(" ")

    valid = []
    for ip in output:
        if ip.find("192.168.") > -1:
            valid.append(ip)
    if len(valid) > 0:
        return valid[0]
    return "UNKOWN"
