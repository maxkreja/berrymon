import threading
import time
from flask import Flask, jsonify, request, abort
from .i2c import I2CDisplay
from .state import State

VERSION_INFO = {
    "name": "Berrymon API 1.0",
    "version": "1.0"
}

app = Flask("Berrymon")
state = State("config.json")

line1 = ""
line2 = ""


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    abort(404)


@app.route("/api", methods=["GET"])
def get_api():
    return jsonify(VERSION_INFO)


@app.route("/api/backlight", methods=["GET", "POST"])
def route_backlight():
    if request.method == "GET" and state.display is not None:
        return get_backlight()
    elif request.method == "GET" and state.display is None:
        abort(501)
    elif request.method == "POST":
        content = request.get_json()
        if verify_set_backlight(content):
            return set_backlight(content["backlight"])
        else:
            abort(501)
    else:
        abort(405)


@app.route("/api/statistics", methods=["GET"])
def get_statistics():
    return jsonify({"username": state.username,
                    "cpu_load": state.load,
                    "cpu_temp": state.temp,
                    "ip": state.ip})


def verify_set_backlight(content):
    return (state.config.enable_lcd
            and content is not None
            and content["backlight"] is not None
            and type(content["backlight"]) is bool)


def get_backlight():
    return jsonify({"backlight": state.display.backlight})


def set_backlight(on: bool):
    state.display.set_backlight(on)
    return get_backlight()


def update_display():
    if state.display is None:
        return

    global line1
    global line2

    l1 = state.ip
    l2 = "{} {}% {}C".format(state.username, int(round(state.load)), int(round(state.temp)))

    if l1 != line1:
        state.display.print_center(l1, 1)
        line1 = l1

    if l2 != line2:
        state.display.print_center(l2, 2)
        line2 = l2


def run_api():
    app.run(host=state.config.host, port=state.config.port)


def run_update():
    while True:
        state.update()
        time.sleep(1)


def run_display():
    while True:
        update_display()
        time.sleep(1)


if __name__ == "__main__":
    flask = threading.Thread(target=run_api)
    flask.start()

    updt = threading.Thread(target=run_update)
    updt.start()

    if state.config.enable_lcd:
        state.add_display(I2CDisplay(state.config.lcd_addr,
                                     state.config.lcd_bus,
                                     state.config.lcd_lines,
                                     state.config.lcd_line_length))
        disp = threading.Thread(target=run_display)
        disp.start()
        disp.join()

    flask.join()
