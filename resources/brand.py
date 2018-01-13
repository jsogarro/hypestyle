from flask_restful import Resource

class BrandIndexResource(Resource):
    def get(self):
        return {'success': True}

class BrandResource(Resource):
    def get(self, id):
        print(id)
        return {'success': True, 'request': id}

    def post(self, id):
        request_json = request.get_json()
        print(request_json)
        return {'success': True, 'request': request_json}

class BrandItemResource(Resource):
    def post(self, id):
        request_json = request.get_json()
        print(request_json)
        return {'success': True, 'request': request_json, 'id': id}
