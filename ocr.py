import numpy as np
import cv2
from PIL import Image
import pytesseract
import os



image = cv2.imread("images/example_01.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)








