import MySQLdb
import mysql.connector

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "",
                           db = "smartShopping")
    c = conn.cursor()

    return c, conn



c,conn = connection()
# c.execute("CREATE TABLE Products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price INT,code VARCHAR(255))")

"""
    @desc Read Code From 'Products' Table by code
    @param {string} code
    @returns {Dictionary}
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
    @desc 
    @param {String} name
    @return {Array}
"""

def readByProductName(name):
    c.execute("SELECT * From Products Where name Like '%{}%'".format(name))
    fields = [field[0] for field in c.description] # List Comprehinsion
    data = c.fetchall()
    dictresult = []
    if len(data) >= 1:
        for d in data:
            product = {}
            for idx,value in enumerate(d):
                product[fields[idx]] = value
            dictresult.append(product)
    return dictresult


def insertBarCodes(barcodes):
    for barcode in barcodes:
        c.execute("INSERT INTO products(code) VALUES ('{}')".format(barcode))
        conn.commit()
    return 'done'