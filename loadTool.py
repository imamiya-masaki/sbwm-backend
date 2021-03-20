from dotenv import load_dotenv
import urllib.request, json
import os
import base64
load_dotenv()
ALLOWED_EXTENSIONS = set(['png', 'jpg'])

def allowed_file(file):
    filename = file.filename
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def helloWorld():
    return 'Hello Wrold'

def simpleOCR(file):
    #とりあえず、一枚の画像をOCRに投げるために
    print(file)
    data = base64.b64encode (file.read())
    to_datas = []
    to_datas.append({'data': data, 'format': 'png', 'name': 'simple'})
    res = postOCR(to_datas)
    print(res)
    return res

def postOCR(getImages = []):
    #getImageは、{data(must),format(any), name(any)}を受け取る
    #getImage = [{},{}...]
    url = os.getenv('APIGW_INVOKE_URL')
    version = "V2"
    requestId = "sbwmRequestId!!"
    timestamp = 0
    lang = 'ja'
    images = []
    uniqueNumber = 0
    for item in getImages:
        postImage = {}
        postImage['format'] = 'png'
        postImage['data'] = item['data']
        if type(item) == 'str':
            #maybe only data?
            postImage['data'] = item
            postImage['name'] = str(uniqueNumber)
            uniqueNumber += 1
        else:
            postImage['data'] = item['data']
            if 'format' in item and item['format'] == 'jpg':
                postImage['format'] = 'jpg'
            if 'name' in item:
                postImage['name'] = item['name']
            else:
                postImage['name'] = str(uniqueNumber)
                uniqueNumber += 1
        images.append(postImage)
    obj = {}
    obj['version'] = version
    obj['requestId'] = requestId
    obj['timestamp'] = timestamp
    obj['lang'] = lang
    obj['images'] = images
    headers = {}
    method = "POST"
    headers['Content-Type'] = 'application/json'
    headers['X-OCR-SECRET'] = os.getenv('SECRET_KEY')
    json_data = json.dumps(obj).encode("utf-8")
    request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
        print('OCR:output', response_body)
        return response_body