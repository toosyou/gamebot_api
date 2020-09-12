from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def receive_control():
    control = request.args.get('control')
    print(control)
    return ''

if __name__ == '__main__':
    app.run(app, host='0.0.0.0', port=80)