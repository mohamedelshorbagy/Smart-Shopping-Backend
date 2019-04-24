import numpy as np
import cv2
from PIL import Image
# import pytesseract
from pyzbar import pyzbar
import os
import json

def readBarOrQrCodes(image_name):
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




# filename = "{}.png".format(os.getpid())
# cv2.imwrite(filename, gray)

# text = pytesseract.image_to_string(Image.open(filename))
# # os.remove(filename)
# print(text)

# cv2.imshow("Image", image)
# cv2.imshow("Output", gray)
# cv2.waitKey(0)


json_data = json.load(open('data.json'))
image_data = readBarOrQrCodes("images/example_04.png")
selectedItem = None
query = "Select * From items where code={}".format(image_data['code'])
for item in json_data:
    if item['code'] == image_data['code']:
        selectedItem = item
        break


print(image_data)
print(selectedItem)
print(selectedItem['price'])







