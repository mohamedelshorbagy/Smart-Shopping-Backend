from flask import Flask
from flask import request
from flask import jsonify
from flask_restplus import Resource, Api
from flask_cors import CORS
import os
from preprocess import preprocess_image
from werkzeug.utils import secure_filename
from DB import readByCode, readByProductName

app = Flask(__name__)
# Enable CORS to avoid cross-origin problem so can web and mobile application use it  
CORS(app)
api = Api(app)

"""
    @method POST
    @desc create new accounts
    @body { <name:string>, <age:int>, <data:{}> }
    @returns {JSON} 
    @TODO
"""

@api.route('/signup')
class SignUp(Resource):
    def post(self, username):
        data = request.get_json()
        return jsonify(data)



"""
    @method POST
    @desc Upload Endpoint for upload image taken by the android app
    @param {File} image
    @returns {JSON} 
"""
@api.route('/upload')
class Upload(Resource):
    def post(self):
        f = request.files['image']
        image_name = 'images/{0}_{1}'.format(os.getpid(),secure_filename(f.filename))
        f.save(image_name)
        data = preprocess_image(image_name)
        rData = []
        if data['code'] is not None:
            result = readByCode(data['code'])
            if bool(result) == True:
                rData.append(result) 
        else:
            result = readByProductName(data['ocr'])
            if len(result) >= 1:
                rData = result

        # TODO:
        # 1. Make a SQL Query to Database to get the Item or related Items
        # 2. Return the Result to the Mobile
        return jsonify({ 'AlgoResult': data, 'data': rData })

if __name__ == '__main__':
    app.run(debug=True, port=5000)