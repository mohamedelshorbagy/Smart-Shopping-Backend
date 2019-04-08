from flask import Flask
from flask import request
from flask import jsonify
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

@api.route('/login/<username>')
class Login(Resource):
    def post(self, username):
        data = request.get_json()
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)