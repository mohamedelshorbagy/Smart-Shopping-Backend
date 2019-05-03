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

"""
@func generate_12_random_numbers()
@dec genertaes  12-digit code for identifing products
@returns {string} barCodeNumber

"""
def generate_12_random_numbers():
    numbers = []
    for x in range(12):
        numbers.append(randrange(10))
    barCodeNumber = ''.join(map(str, numbers))
    return barCodeNumber

# for i in range(40):
#     barCodeNumber = generate_12_random_numbers()
#     generate_barcode(barCodeNumber)

"""
@func getAllFilesFromDir(dirName) 
@desc get all barcodes from certain folder ,extract filenames (code) 
and appends them to a list of filenames
@param {string} dirname
@returns {list} fileNamesPure

"""
def getAllFilesFromDir(dirName):
    fileNames = os.listdir(dirName)
    fileNamesPure = []
    for fName in fileNames:
        fileNamesPure.append(os.path.splitext(fName)[0])
    return fileNamesPure

#filling the codes in the database
#genterate a list of all codes from barcode dir
barcodes = getAllFilesFromDir('barcodes')
#fill the product code value in the database with the codes "barcodes"
data = insertBarCodes(barcodes)
#print(data)