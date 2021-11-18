import sys
import time
from http.client import HTTPException

from flask import Flask, jsonify, request
from blinkt import set_brightness, set_pixel, show, clear, get_pixel, NUM_PIXELS
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Blinkt! API'

@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code

    set_brightness(0.1)

    set_pixel(0, 255, 0, 0)
    set_pixel(1, 255, 165, 0)
    set_pixel(2, 255, 0, 0)
    set_pixel(3, 255, 165, 0)
    set_pixel(4, 255, 0, 0)
    set_pixel(5, 255, 165, 0)
    set_pixel(6, 255, 0, 0)
    set_pixel(7, 255, 165, 0)
    show()

    time.sleep(0.25)

    set_pixel(0, 255, 165, 0)
    set_pixel(1, 255, 0, 0)
    set_pixel(2, 255, 165, 0)
    set_pixel(3, 255, 0, 0)
    set_pixel(4, 255, 165, 0)
    set_pixel(5, 255, 0, 0)
    set_pixel(6, 255, 165, 0)
    set_pixel(7, 255, 0, 0)
    show()

    time.sleep(0.25)

    set_pixel(0, 255, 0, 0)
    set_pixel(1, 255, 165, 0)
    set_pixel(2, 255, 0, 0)
    set_pixel(3, 255, 165, 0)
    set_pixel(4, 255, 0, 0)
    set_pixel(5, 255, 165, 0)
    set_pixel(6, 255, 0, 0)
    set_pixel(7, 255, 165, 0)
    show()

    time.sleep(0.25)

    set_pixel(0, 255, 165, 0)
    set_pixel(1, 255, 0, 0)
    set_pixel(2, 255, 165, 0)
    set_pixel(3, 255, 0, 0)
    set_pixel(4, 255, 165, 0)
    set_pixel(5, 255, 0, 0)
    set_pixel(6, 255, 165, 0)
    set_pixel(7, 255, 0, 0)
    show()

    time.sleep(0.25)

    return jsonify(error=str(e)), code

@app.route('/red')
def set_red():
    set_brightness(0.5)

    for x in range(NUM_PIXELS):
        set_pixel(x, 255, 0, 0)
        show()

        data = {
            "status": 200,
            "message": "Lights are now red"
        }

    return jsonify(data)

@app.route('/yellow')
def set_yellow():
    set_brightness(0.5)

    for x in range(NUM_PIXELS):
        set_pixel(x, 255, 255, 0)
        show()

        data = {
            "status": 200,
            "message": "Lights are now yellow"
        }

    return jsonify(data)

@app.route('/green')
def set_green():
    set_brightness(0.5)

    for x in range(NUM_PIXELS):
        set_pixel(x, 0, 255, 0)
        show()

        data = {
            "status": 200,
            "message": "Lights are now green"
        }

    return jsonify(data)

@app.route('/blue')
def set_blue():
    set_brightness(0.5)

    for x in range(NUM_PIXELS):
        set_pixel(x, 0, 0, 255)
        show()

        data = {
            "status": 200,
            "message": "Lights are now blue"
        }

    return jsonify(data)

@app.route('/off')
def turn_off():
    set_brightness(0)

    for x in range(NUM_PIXELS):
        set_pixel(x, 0, 0, 0)
        show()

        data = {
            "status": 200,
            "message": "Lights are now off"
        }

    return jsonify(data)

@app.route('/on')
def turn_on():
    set_brightness(1)

    for x in range(8):
        set_pixel(x, 255, 255, 255)
        show()

        data = {
            "status": 200,
            "message": "Lights are now on"
        }

    return jsonify(data)

@app.route('/custom', methods=['POST'])
def turn_custom():
    data = request.get_json()

    for x in data:
        print(jsonify(x), file=sys.stderr)
        set_pixel(x['led'], x['red'], x['green'], x['blue'])
        show()

    data = {
        "status": 200,
        "message": "Custom pattern applied"
    }

    return jsonify(data)

@app.route('/status', methods=['GET'])
def report_status():
    pixel_status = []
    for i in range(NUM_PIXELS):
        pixel_status.append(dict(Pixel=i, Status=dict(zip(["Red","Green","Blue","Brightness"],get_pixel(i)))))
    data = {
        "status": 200,
        "message": pixel_status
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
