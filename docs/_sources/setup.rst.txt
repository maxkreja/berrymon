Setup
=====

In order to use Berrymon, you will need to install some dependencies
and make some configurations to your system. If you want to, you can connect
an LCD display and make Berrymon use it. All required steps should be performed 
in the same order as they are described here. If you don't want to use an LCD,
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

    sudo apt install python3 python3-pip

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

That's all you have to do in order to install Berrymon. Now it's time to configure and start it. Head on to the next section.

Configuration
-------------

There are some changes you need to make to the configuration before you can finally launch Berrymon. There is a folder
called src in the Berrymon root directory, in it you will find a file called 'config.json'. This has to be edited to
adjust Berrymon to your system configuration.

.. code-block:: json
    :caption: Default contents of the configuration file

    {
        "host": "0.0.0.0",
        "port": 2374,
        "enable_lcd": true,
        "lcd_addr": "0x27",
        "lcd_bus": 1,
        "lcd_lines": 2,
        "lcd_line_length": 16
    }

The options and what they are doing are described in the following:

*All options regarding the LCD display are irrelevant until 'enable_lcd' is set to true.*

- **host:** The address for the API to listen on, set it to *0.0.0.0* to listen on all addresses
- **port:** The port for the API to listen on, self explanatory
- **enable_lcd:** Tells Berrymon if an LCD should be used or not, this must be set to false if no LCD is connected
- **lcd_addr:** The address of the display, the section :ref:`lcd-conn-setup` explains where to find the address (if the address of you display is just an integer like '27', just ad '0x' in front if it: '0x27')
- **lcd_bus:** Leave this on '1' if you got only a single display connected, if you got multiple display controllers you have to adjust this
- **lcd_lines:** The amount of lines the connected LCD display has
- **lcd_line_length:** The amount of characters that fit on one line of your display

This means that the default configuration from above would mean the following:

- :code:`"host": "0.0.0.0"`: listen on all addresses
- :code:`"port": 2374`: listen on port 2374
- :code:`"enable_lcd": true`: enable the LCD display
- :code:`"lcd_addr": "0x27"`: according to :ref:`lcd-conn-setup` the address of the display is '27'
- :code:`"lcd_bus": 1`: the bus number is '1', we only got one controller connected
- :code:`"lcd_lines": 2`: our display has two lines
- :code:`"lcd_line_length": 16`: there are 16 characters on each line of our display

Launch
------

To start Berrymon you need to be in the root directory of Berrymon. You should see a file tree like this:

.. code-block:: bash
    :caption: Berrymon root directory

    ┌ docs
    ├ sphinx
    ├ src
    ├ .gitignore
    ├ LICENSE.md
    ├ README.md
    └ requirements.txt

Navigate to the 'src' directory :code:`cd src`. To start Berrymon type this command: :code:`python3 -m berrymon`.
That's all it takes to start Berrymon manually. The API should now be running and listening on the address and port
you specified in the config file, if you connected and enabled an LCD display, this should turn on and display
some information.

*Note:* If you want to save some storage space you can delete the 'sphinx' folder. If you don't need the documentation
on your disc you can delete the 'docs' folder too.

Autostart
~~~~~~~~~

*Coming soon*