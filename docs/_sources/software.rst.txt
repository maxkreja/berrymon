Software Setup
==============

To use Berrymon you have to do some configurations and install some
dependencies. 

**If you don't want to use an LCD display you can skip the** :ref:`display-setup`
**part and can continue with the** :ref:`berrymon-setup` **part.**

.. _display-setup:

Display Setup
-------------

Before you start make sure you have read the guide on how to connect a
display to your Raspberry Pi: :doc:`hardware`. If you have done this, continue here.

First you need to get access to a terminal. Then we will install the following requirements:

* `Python 3 <https://www.python.org/>`_
* `i2c-tools <https://i2c.wiki.kernel.org/index.php/I2C_Tools>`_
* `smbus2 <https://pypi.org/project/smbus2/>`_

If you need to install all of them or if you are not sure if you got everything together,
execute the following commands in your terminal:

.. code-block:: bash
   :caption: Install Python 3 and i2c-tools
   
   sudo apt install python3 i2c-tools

.. code-block:: bash
   :caption: Install smbus2

   python3 -m pip install smbus2

Those commands will download and install any of the dependencies if they are missing or out of date.
After you have done this, you are ready to configurate your system. You have to edit a sytem file
that allows your Raspberry Pi to load the display driver at boot, to do so open the file in the text-editor
nano by using this command:

.. code-block:: bash

   sudo nano /etc/modules

The contents of the file should look like this, if they don't just copy and paste the following text:

.. code-block:: bash

   # /etc/modules: kernel modules to load at boot time.
   #
   # This file contains the names of kernel modules that should be loaded
   # at boot time, one per line. Lines beginning with "#" are ignored.

   i2c-dev

Now at the end of the file add a new line so the file will look like this:

.. code-block:: bash

   # /etc/modules: kernel modules to load at boot time.
   #
   # This file contains the names of kernel modules that should be loaded
   # at boot time, one per line. Lines beginning with "#" are ignored.

   i2c-dev
   i2c-bcm2708 # You've added this line

Save the file by pressing **CTRL + O**, type *yes* or *y* and confirm by pressing **ENTER**,
then exit the editor by pressing **CTRL + X**. Reboot your Raspberry Pi by executing :code:`sudo reboot`.

**WIP**

.. _berrymon-setup:

Berrymon Setup
--------------

**WIP**