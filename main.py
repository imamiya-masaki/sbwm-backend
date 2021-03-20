from flask import *
from loadTool import *
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def route():
    return helloWorld()

@app.route('/load', methods=["GET", "POST"])
def load():
    output = {}
    if request.method ==  'POST':
        if 'img_file' not in request.files:
            output['status'] = 400
            output['error'] = 'img_file not in request'
        elif not allowed_file(request.files['img_file']):
            output['status'] = 400
            output['error'] = 'can use extension type'
        else:
            #success
            img_file = request.files['img_file']
            filename = secure_filename(img_file.filename)
            print('args', request)

