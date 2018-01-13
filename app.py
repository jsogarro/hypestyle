from flask import Flask, request, render_template
from flask_restful import Api

from resources.brand import Brand, BrandsIndex, BrandItem

app = Flask(__name__)
api = Api(app)

# GET /
@app.route('/')
def home():
    return render_template('index.html')

api.add_resource(BrandsIndex, '/brands')
api.add_resource(Brand, '/brands/<string:id>')
api.add_resource(BrandItem, '/brands/<string:id>/item')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
