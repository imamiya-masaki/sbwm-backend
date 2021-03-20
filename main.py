from flask import *
from loadTool import *
from werkzeug.utils import secure_filename
import base64
import json
app = Flask(__name__)

if __name__ == '__main__':
 app.run(debug=True)

@app.route('/')
def route():
    return helloWorld()

@app.route('/load', methods=["GET", "POST"])
def load():
  output = {}
  if request.method ==  'POST':
    # if 'img_file' not in request.files:
    #   output['status'] = "400"
    #   output['error'] = 'img_file not in request'
#       elif not allowed_file(request.form['img_file']):
#         output['status'] = 400
#           output['error'] = 'can use extension type'
    # else:
      #success
      #img_file = request.form['img_file']
      #filename = secure_filename(img_file.filename)
    print("take:Data", request.json)
    img = request.json["img_file"]
    output['status'] = "200"
    output['data'] = simpleOCR(img)
    data = request
    #print('args', request,data.values.get('img_file'), request.json["img_file"])
    #return json.dumps({'status': "200"})
    return  json.dumps(output)
   
