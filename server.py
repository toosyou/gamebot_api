from flask import Flask
from flask import request
import configparser
from threading import Lock

from ahk import AHK

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.cfg')
avaliable_controls = [name for name, value in config.items('control')]

ahk = AHK()
window = ahk.find_window(title=config['general']['title'].encode())
control_lock = Lock()

def press(key="", window=window):
    global control_lock
    with control_lock:
        window.send(key, press_duration=110, block=True)

@app.route('/', methods=['GET'])
def receive_control():
    control = request.args.get('control')

    if control in avaliable_controls:
        press(config['control'][control])

    return ''

if __name__ == '__main__':
    window.activate()
    app.run(host='0.0.0.0', port=80)