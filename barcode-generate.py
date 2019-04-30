import barcode
from barcode.writer import ImageWriter
from random import randrange
import os
from DB import insertBarCodes

"""
    @func generate_barcode(code)
    @desc Generate Barcode based on code passed  to it 
    @param {Number|String} code [must be 12 numbers]
    @returns {void} [save image to barcodes/]
"""

def generate_barcode(code):
    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(code, writer=ImageWriter())
    fullname = ean.save('barcodes/{}'.format(code))

def generate_12_random_numbers():
    numbers = []
    for x in range(12):
        numbers.append(randrange(10))
    barCodeNumber = ''.join(map(str, numbers))
    return barCodeNumber

# for i in range(40):
#     barCodeNumber = generate_12_random_numbers()
#     generate_barcode(barCodeNumber)


def getAllFilesFromDir(dirName):
    fileNames = os.listdir(dirName)
    fileNamesPure = []
    for fName in fileNames:
        fileNamesPure.append(os.path.splitext(fName)[0])
    return fileNamesPure


barcodes = getAllFilesFromDir('barcodes')
data = insertBarCodes(barcodes)
print(data)