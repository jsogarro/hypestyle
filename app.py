from flask import Flask, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# GET /
@app.route('/')
def home():
    return render_template('index.html')

class BrandsIndex(Resource):
    def get(self):
        return {'success': True}

class Brand(Resource):
    def get(self, id):
        print(id)
        return {'success': True, 'request': id}

    def post(self, id):
        request_json = request.get_json()
        print(request_json)
        return {'success': True, 'request': request_json}

class BrandItem(Resource):
    def post(self, id):
        request_json = request.get_json()
        print(request_json)
        return {'success': True, 'request': request_json, 'id': id}

api.add_resource(BrandsIndex, '/brands')
api.add_resource(Brand, '/brands/<string:id>')
api.add_resource(BrandItem, '/brands/<string:id>/item')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
