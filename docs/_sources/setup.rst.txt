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

Berrymon is written in Python, hence it requires `Python <https://www.python.org>`_ to work. If you
haven't installed Python 3 yet, run these commands to install it. In case Python 3 is already installed, it
won't change anything:

.. code-block:: bash
    :caption: Install Python 3 using *apt*

    sudo apt install python3 python3-pip

Berrymon needs some Python libraries to work, you can install them right now or use the *requirements.txt*
file described in :ref:`Installation`:

.. code-block:: bash
    :caption: Install Python libraries using *pip*

    python3 -m pip install psutil smbus2 flask

As you're done with setting up Python, you either can continue by setting up the LCD display
or with the installation of Berrymon in case you don't want to use one.

.. _lcd-conn-setup:

LCD Connection & Setup
----------------------

*A guide on how to connect your display to the Raspberry Pi in terms of hardware will come in the near future, 
for now please refer to this* `guide <http://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming>`_ *.*

**If you are using the guide above, there is no need to install the python-smbus package, but do take note of the 
display address because you will need it later. Berrymon includes all the code to communicate with the LCD, so you can 
stop reading the guide above when it comes to programming the LCD.**

Installation
------------

The easiest way to install Berrymon is to clone the `repository <https://github.com/maxkreja/berrymon>`_ from GitHub. 
Make sure that `git <https://git-scm.com/>`_ is installed on your system, then clone the repository with the following command.

.. code-block:: bash
    :caption: Clone the latest version from GitHub

    git clone https://github.com/maxkreja/berrymon.git berrymon

Executing the command above, a new folder called ‘berrymon’ will be created into your current directory and Berrymon 
will be downloaded into it. It’s recommended to download Berrymon to your home directory, so this guide always refers 
to the files in it. If you didn’t, keep your chosen directory in mind, since you will need it later if you want to make 
Berrymon start automatically as your Pi boots.

**Skip the next step if you already installed the Python dependencies in** :ref:`system-deps`

Now just install the Python dependencies by changing the directories and installing a 'requirements.txt' file. Assuming you are 
in the directory where you downloaded Berrymon and you got a folder called 'berrymon', execute the following commands:

.. code-block:: bash
    :caption: Install Python dependencies

    cd berrymon
    python3 -m pip install -r requirements.txt

That’s all you have to do in order to install Berrymon!

Now it’s time to configure Berrymon and get it up and running. Head on to the next section.

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

To start Berrymon you need to be in the previously defined root directory. You should see a file tree like this:

.. code-block:: bash
    :caption: Berrymon root directory

    ┌ docs
    ├ sphinx
    ├ src
    ├ .gitignore
    ├ LICENSE.md
    ├ README.md
    └ requirements.txt

Navigate to the ‘src’ directory :code:`cd src`. By executing this command, Berrymon will start: :code:`python3 -m berrymon`. 
That’s all it takes to start Berrymon manually. The API should now be listening on the address and port 
you specified in the config file, if you connected and enabled the LCD display, it should turn on and display 
some information.

*Note:* If you want to save some storage space you can delete the 'sphinx' folder. If you don't need the documentation
on your disc you can delete the 'docs' folder too.

Autostart
~~~~~~~~~

If you want to make Berrymon start at system boot, you need to place a script with the following content in your home directory:

.. code-block:: bash
    :caption: Autostart script

    #!/bin/bash

    TARGET="/home/[user]/berrymon/src"
    export PYTHONPATH="$PYTHONPATH:$TARGET"

    cd $TARGET
    python3 -m berrymon

Just place a new file in your home directory with the command :code:`touch berrymon.sh`, paste in the content above and 
replace :code:`[user]` with the actual username (should be ‘pi’ by default). If you didn’t download Berrymon to you home 
directory as described in :ref:`Installation`, you have to adjust the :code:`TARGET` variable accordingly.

Now we need to create a cronjob that executes this script at boot, to do this run :code:`crontab -e`, if you are asked to
select an editor, select nano. At the end of the file insert a new line and add the
following code, replacing :code:`[user]` with the actual username:

Now we have to create a cronjob that executes this script at boot, to do this run :code:`crontab -e`, if you are asked to 
select an editor, select nano. At the end of the file, insert a new line and add the following code, 
replacing :code:`[user]` with the actual username:

.. code-block:: bash
    :caption: Add a cronjob to start Berrymon

    @reboot /home/[user]/berrymon.sh

Save the file and exit. Berrymon should start with each system boot from now on.
