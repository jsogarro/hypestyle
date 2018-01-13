from flask_restful import Resource

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
