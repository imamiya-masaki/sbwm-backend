from dotenv import load_dotenv
import urllib.request, json
import os
import requests
import base64
import cloudinary as Cloud
from cutOut import *
Cloud.config.update = ({
	'cloud_name':os.environ.get('CLOUDINARY_CLOUD_NAME'),
  'api_key': os.environ.get('CLOUDINARY_API_KEY'),
  'api_secret': os.environ.get('CLOUDINARY_API_SECRET')
})
load_dotenv()
ALLOWED_EXTENSIONS = set(["png", "jpg"])

def allowed_file(file):
    filename = file.filename
    return "." in filename and \
        filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS

def helloWorld():
  return "Hello Wrold2"

def simple2OCR(url):
	response = requests.get(url)
	file = response.content
	res = imageRe(file)
	output = {'red': {}, 'blue': {}, 'green': {}, 'Black': {}}
	for key in res:
		#print('kmdkwamkda', key)
		output[key]['text'] = []
		output[key]['square'] = []
		text = simpleTo(res[key]["text"])
		#output[key]['text'] = text
		if "images" in text:
			#print("item", text["images"])
			for image in text["images"]:
				if "fields" in image:
					for item in image["fields"]:
						if "inferText" in item:
							output[key]['text'].append(item["inferText"])
		if not key == "Black":
			square = simpleTos(res[key]["square"])
			if "images" in square:
				for image in square["images"]:
					if "fields" in image:
						for item in image["fields"]:
							if "inferText" in item:
								output[key]['square'].append(item["inferText"])
			#output[key]['square'] = square
	print("end!!!!")
	return output
			
def simpleTo(binary):
	to_datas = []
	to_datas.append({"data": binary.decode('utf-8'), "format": "png", "name": "simple"})
	res = postOCR(to_datas)
	return res.json()
def simpleTos(binarys):
	to_datas = []
	for item in binarys:
		to_datas.append({"data": item.decode('utf-8'), "format": "png", "name": "simple"})
	res = postOCR(to_datas)
	return res.json()
def simpleOCR(url):
	#とりあえず、一枚の画像をOCRに投げるために
	#print(file)
	response = requests.get(url)
	file = response.content
	data = base64.b64encode(file).decode('utf-8')
	to_datas = []
	to_datas.append({"data": data, "format": "png", "name": "simple"})
	print("REREQQQ", "aa")
	res = postOCR(to_datas)
	print("REREQQQ",res, res.json())
	return res.json()

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
    print("RESRES")
    json_data = json.dumps(obj).encode("utf-8")
    request = requests.post(url, data=json_data, headers=headers)
    return request