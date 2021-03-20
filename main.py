from flask import *
app = Flask(__name__)

@app.route('/')
def route():
    name = "Hello World"
    return name

@app.route('/load', methods=["GET", "POST"])
def load():
    if request.method ==  'POST':
        img_file = request.files['img_file']
        print('args', request)

