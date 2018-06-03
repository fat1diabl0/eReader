# all Google OCR related code goes in here. 
# needs google-cloud-vision package. Will be moved to a separate requirements file. 

import io
import os

from base64 import b64encode
import json
import requests

# from google.cloud import vision
# from google.cloud.vision import types

# client = vision.ImageAnnotatorClient()

# # Input: Image filepath, Output: formatted string.
# def performGoogleOCR(inputImagePath):
#     file_name = inputImagePath
#     with io.open(file_name, 'rb') as image_file:
#         content = image_file.read()
#     image = types.Image(content=content)
#     response = client.document_text_detection(image=image) #use google's document text ocr. 
#     text_response = response.full_text_annotation
#     return text_response.text

URL = 'https://vision.googleapis.com/v1/images:annotate'
API_KEY = "AIzaSyBn0724N8H0wOh9CcHqnkIUof-1qdxAaUE"

def request_ocr(imgname):
	img_requests = ""
	with open(imgname, 'rb') as f:
		ctxt = b64encode(f.read()).decode()
		img_requests = { 'image': {'content': ctxt},
                         'features': [{
                        'type': 'TEXT_DETECTION',
                        'maxResults': 1}] }
        
	
	requestData = json.dumps({"requests":img_requests}).encode()
	response = requests.post(URL,data=requestData,params={'key': API_KEY},headers={'Content-Type': 'application/json'})
	return response

def performGoogleOCR(inputImagePath):
    response = request_ocr(inputImagePath)
    
    if response.status_code != 200 or response.json().get('error'):
        print(response.text)
        return ""
    else:
        for idx, resp in enumerate(response.json()['responses']):
                if 'textAnnotations' in resp.keys():
                    t = resp['textAnnotations'][0]
                    return t['description']
                else:
                    return ""
