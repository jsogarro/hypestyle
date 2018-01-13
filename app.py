from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# GET /
@app.route('/')
def home():
    return render_template('index.html')

# GET /brands
@app.route('/brands')
def get_brands():
    return jsonify({'success': True})

# GET /brands/:id
@app.route('/brands/<string:id>')
def get_brand(id):
    return jsonify({'success': True})

# POST /brands
@app.route('/brands', methods=['POST'])
def create_brand():
    req = request.get_json()
    return jsonify({'success': True, 'brand': req})

# POST /brands/:id/item
@app.route('/brands/<string:id>/item', methods=['POST'])
def get_item_in_brand(id):
    return jsonify({'success': True})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
