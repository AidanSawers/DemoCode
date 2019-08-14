from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Techlauncher Demo :)'

@app.route('/hello')
def hello():
    return 'hello'

@app.route('/hello_name')
def hello_name():
    name = request.args.get("name")
    return 'Hello '+name+"!"

if __name__ == '__main__':
    app.run()