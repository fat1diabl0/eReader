# all Google OCR related code goes in here. 
# needs google-cloud-vision package. Will be moved to a separate requirements file. 

import io
import os

from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()

# Input: Image filepath, Output: formatted string.
def performGoogleOCR(inputImagePath):
    file_name = inputImagePath
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.document_text_detection(image=image) #use google's document text ocr. 
    text_response = response.full_text_annotation
    return text_response.text


