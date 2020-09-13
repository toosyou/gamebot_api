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

def press(key="", window=window, repeat=1):
    global control_lock
    with control_lock:
        window.send(key*repeat, press_duration=110, blocking=True)

@app.route('/', methods=['GET'])
def receive_control():
    control = request.args.get('control')
    repeat = request.args.get('repeat') if request.args.get('repeat') is not None else 1

    if control in avaliable_controls:
        press(config['control'][control], repeat=repeat)

    return ''

if __name__ == '__main__':
    window.activate()
    app.run(host='0.0.0.0', port=80)