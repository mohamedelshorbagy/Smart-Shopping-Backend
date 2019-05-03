import MySQLdb
import mysql.connector

"""
    @func connection()
    @desc using  MySQLdb creating a connection with the store database
    @returns {cursor and connection objects} c,conn
"""

def connection():
    conn = MySQLdb.connect(host="localhost", user = "root",passwd = "",db = "smartShopping")
    c = conn.cursor()
    return c, conn

#creating the connection to mysql database
c,conn = connection()

"""
    @func readByCode(code)
    @desc select product data by Reading Code From "Products" Table in the database
    @param {string} code
    @returns {Dictionary} dictresult
"""

def readByCode(code):
    c.execute("SELECT * FROM products WHERE code='{}'".format(code))
    fields = [field[0] for field in c.description] # List Comprehinsion
    data = c.fetchone()
    dictresult = {}
    if data is not None:    
        for index, d in enumerate(list(data)):
            dictresult[fields[index]] = d
    return dictresult

"""
    @func readByProductName(name)
    @desc select product data by Reading product name From "Products" Table in the database
    @param {String} name
    @return {Array} result
"""

def readByProductName(name):
    c.execute("SELECT * From Products Where name Like '%{}%'".format(name))
    fields = [field[0] for field in c.description] # List Comprehinsion
    data = c.fetchall()
    result = []
    if len(data) >= 1:
        for d in data:
            product = {}
            for idx,value in enumerate(d):
                product[fields[idx]] = value
            result.append(product)
    return result
"""
@func GetproductData (code,name)
@desc interfaces the database output whether by code or by name to the mobile application
@param {string} code,name
@returns {dictionary} 
"""

def GetproductData (code,name):
    productbycode=readByCode(code)
    productbyname=readByProductName(name)
    if productbycode !=None:
     return productbycode
    elif productbyname !=None:
        return productbyname
    

"""
@func insertBarCodes(barcodes)
@desc insert Barcode for products into "product" table in the database
@param {List} barcodes
@returns {string} done

"""


def insertBarCodes(barcodes):
    for barcode in barcodes:
        c.execute("INSERT INTO products(code) VALUES ('{}')".format(barcode))
        conn.commit()
    return 'done'

# c.execute("CREATE TABLE Products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price INT,code VARCHAR(255))")