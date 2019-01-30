API
===

Berrymons HTTP API is its core feature. If you want to use it outside 
of the Berrymon mobile app, take at the look at it’s documentation.

The API uses GET and POST requests in combination with JSON encoded data. 
The default HTTP codes are used for error handling.

:code:`<host>` and :code:`<port>` are system specific and depend on your 
configuration. If a request was sent with the wrong method, *405* will be returned. 
All display related requests will return *501* if the display is disabled by the config.


GET Requets
-----------

:code:`<host>:<port>/`: 

- Base URL
- Use this to ping for up/down monitoring
- **Returns:** *404*

|

:code:`<host>:<port>/api`:

- Base API URL
- **Returns:** API version information:

.. code-block:: json

    {
        "name": "Berrymon API 1.0",
        "version": "1.0"
    }

|

:code:`<host>:<port>/api/backlight`:

- Get display backlight status
- **Returns:** Backlight status or *501*:

.. code-block:: json

    {"backlight": true}

|

:code:`<host>:<port>/api/statistics`:

- Get system statistics
- **Returns:** Statistics:

.. code-block:: json

    {
        "username": "john",
        "cpu_load": 45.32,
        "cpu_temp": 65.2,
        "ip": "192.168.4.5"
    }

POST requests
-------------

:code:`<host>:<port>/api/backlight`:

- Set display backlight
- **POST Data:** Desired backlight status (on = *true*, off = *false*):

.. code-block:: json

    {"backlight": true}

- **Returns:** Backlight status or *501*:

.. code-block:: json

    {"backlight": true}

|