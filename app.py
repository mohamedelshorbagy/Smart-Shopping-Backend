from flask import Flask
from flask import request
from flask import jsonify
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

"""
    @method GET
    @description hello endpoint for testing
    @param {Dict} self
    @returns {JSON}
"""
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    
"""
    @method POST
    @desc Login Endpoint for login by username
    @param {string} username
    @body { <name:string>, <age:int>, <data:{}> }
    @returns {JSON} 
"""

@api.route('/login/<username>')
class Login(Resource):
    def post(self, username):
        data = request.get_json()
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)