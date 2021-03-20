from dotenv import load_dotenv
import urllib.request, json
import os
import requests
import base64
load_dotenv()
ALLOWED_EXTENSIONS = set(["png", "jpg"])

def allowed_file(file):
    filename = file.filename
    return "." in filename and \
        filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS

def helloWorld():
    return "Hello Wrold2"

def simpleOCR(file):
    #とりあえず、一枚の画像をOCRに投げるために
    print(file)
    data = base64.b64encode(file.read()).decode('utf-8')
    to_datas = []
    to_datas.append({"data": data, "format": "png", "name": "simple"})
    res = postOCR(to_datas)
    print(res, res.json())
    return json.dumps(res.json()).encode("utf-8")

def postOCR(getImages = []):
    #getImageは、{data(must),format(any), name(any)}を受け取る
    #getImage = [{},{}...]
    url = os.getenv("APIGW_INVOKE_URL")
    version = "V2"
    requestId = "sbwmRequestId!!"
    timestamp = "0"
    lang = "ja"
    images = []
    uniqueNumber = 0
    for item in getImages:
        postImage = {}
        postImage["format"] = "png"
        postImage["data"] = item["data"]
        if type(item) == "str":
            #maybe only data?
            postImage["data"] = item
            postImage["name"] = str(uniqueNumber)
            uniqueNumber += 1
        else:
            postImage["data"] = item["data"]
            if "format" in item and item["format"] == "jpg":
                postImage["format"] = "jpg"
            if "name" in item:
                postImage["name"] = item["name"]
            else:
                postImage["name"] = str(uniqueNumber)
                uniqueNumber += 1
        #postImage["data"] = "" # 仮
        images.append(postImage)
    obj = {}
    obj["version"] = version
    obj["requestId"] = requestId
    obj["timestamp"] = timestamp
    obj["lang"] = lang
    obj["images"] = images
    headers = {}
    method = "POST"
    headers["Content-Type"] = "application/json"
    headers["X-OCR-SECRET"] = os.getenv("SECRET_KEY")
    print()
    json_data = json.dumps(obj).encode("utf-8")
    request = requests.post(url, data=json_data, headers=headers)
    return request
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)