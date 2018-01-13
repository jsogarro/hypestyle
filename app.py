from flask import Flask, request, render_template
from flask_restful import Api

from resources.brand import BrandResource, BrandIndexResource, BrandItemResource

app = Flask(__name__)
api = Api(app)

# Home
@app.route('/')
def home():
    return render_template('index.html')

# Brand
api.add_resource(BrandIndexResource, '/brands')
api.add_resource(BrandResource, '/brands/<string:id>')
api.add_resource(BrandItemResource, '/brands/<string:id>/item')

if __name__ == '__main__':
    from config.db import db
    app.run(port=5000, debug=True)
