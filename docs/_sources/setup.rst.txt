Setup
=====

In order to use Berrymon, you will need to install some dependencies
and make some configurations to your system. If you want to, you can connect
an LCD display and make Berrymon use it. All required steps should be performed 
in the same order as they are described here. Of you don't want to use an LCD,
skip the related steps.

The latest version of `Raspbian OS <https://www.raspberrypi.org/downloads/raspbian/>`_ is required for setting up Berrymon.

1. :ref:`system-deps`
2. :ref:`lcd-conn-setup`
3. :ref:`Installation`
4. :ref:`Configuration`
    4.1 :ref:`Autostart`

.. _system-deps:

System & Dependencies
---------------------

Berrymon is written in `Python <https://www.python.org>`_ and requires Python 3 to work. If you
don't have Python 3 installed or are not sure if you got it, run this commands to install. In case
Python 3 is already installed, it wont change anything:

.. code-block:: bash
    :caption: Install Python 3 using *apt*

    sudo apt install python3

Berrymon needs some Python libraries, you can install them now or use the *requirements.txt*
file described in :ref:`Installation`:

.. code-block:: bash
    :caption: Install Python libraries using *pip*

    python3 -m pip install psutil smbus2 flask

When you are done with this, you can continue by setting up an LCD display or the installation
of Berrymon if you don't want to use one.

.. _lcd-conn-setup:

LCD Connection & Setup
----------------------

*A guide on how to connect your display to the Raspberry Pi in terms of
hardware will come in the near future, for now take a look at this* `guide <http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming>`_.

**If you use the guide above, you don't need to install the python-smbus package. Just make note of the display 
address because you will need this later. Stop with the guide linked above when it comes to programming the LCD.
Berrymon includes all the code to talk with the LCD.**

Installation
------------

The easiest way to install Berrymon ist to clone the `repository <https://github.com/maxkreja/berrymon>`_ from GitHub. 
Make sure that `git <https://git-scm.com/>`_ is installed on your system, then clone the repository with the following
command.

.. code-block:: bash
    :caption: Clone the latest version from GitHub

    git clone https://github.com/maxkreja/berrymon.git berrymon

The command above will download Berrymon into a new folder called 'berrymon' at your current directory. It's recommended
to download Berrymon to your home directory and this guide will assume you did that. If you didn't, remember the location
as you will need it later if you want to make Berrymon start automatically when your Raspberry Pi boots.

**Skip the next step if you already installed the Python dependencies in** :ref:`system-deps`

Now just install the Python dependencies by changing dirs and installing a *requirements.txt* file. Assuming you are in the directory
where you downloaded Berrymon and you got a folder called *berrymon*, execute the following commands:

.. code-block:: bash
    :caption: Install Python dependencies

    cd berrymon
    python3 -m pip install -r requirements.txt

That's all you have to do in order to install Berrymon. Now it's time to configre and start it. Head on to the next section.

Configuration
-------------

Autostart
~~~~~~~~~