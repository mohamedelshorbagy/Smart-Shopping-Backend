import numpy as np
import cv2
from PIL import Image
import pytesseract
from pyzbar import pyzbar
import os
import json

"""
    @desc using pyzbar libray to read [QR,Bar] Codes from Images and extract thier content
    @param {string} image_name
    @returns {JSON}
"""
def qr_bar_code(image_name):
    image = cv2.imread(image_name)
    barcodes = pyzbar.decode(image)
    data = { 'type': None, 'code': None }
    for barcode in barcodes:
        # extract the bounding box location of the barcode and draw the
        # bounding box surrounding the barcode on the image
        # (x, y, w, h) = barcode.rect
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # the barcode data is a bytes object so if we want to draw it on
        # our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        data['type'] = barcodeType
        data['code'] = barcodeData    
    return data

"""
    @desc using tessract to read letters and words in images
    @param {string} image_name
    @returns {JSON}
"""
def OCR(image_name):
    image = cv2.imread(image_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    if len(text) == 0:
        text = None
    return text




"""
    @desc preprocess_image is an interface fn to [qr_bar_code, OCR]
    @param {string} image_name
    @returns {JSON}
"""
def preprocess_image(image_name):
    image_data = qr_bar_code(image_name)
    image_ocr = OCR(image_name)
    return { 'ocr': image_ocr, 'code': image_data['code'] }


# json_data = json.load(open('data.json'))
# image_data = readBarOrQrCodes("images/example_01.png")
# image_ocr = OCR("images/example_01.png")
# selectedItem = None
# query = "Select * From items where code={}".format(image_data['code'])
# for item in json_data:
#     if item['code'] == image_data['code']:
#         selectedItem = item
#         break

# print(preprocess_image("images/example_01.png"))
# print('QR Code Result:')
# print(image_data)
# print('OCR Result:')
# print(image_ocr)






