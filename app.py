from flask import Flask, jsonify

app = Flask(__name__)

# GET /
@app.route('/')
def home():
    return "Hello Page"

# GET /brands
@app.route('/brands')
def get_brands(name):
    pass

# GET /brands/:id
@app.route('/brands/<string:id>')
def get_brand(name):
    pass

# POST /brands
@app.route('/brands', methods=['POST'])
def create_brand():
    pass

# POST /brands/:id/item
@app.route('/brands/<string:id>/item', methods=['POST'])
def get_item_in_brand():
    pass

if __name__ == '__main__':
    app.run(port=5000)
