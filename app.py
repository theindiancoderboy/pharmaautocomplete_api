from flask import Flask, jsonify,request

app = Flask(__name__)


items = []

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json.get('item')
    if item:
        items.append(item)
        return jsonify({'message': 'Item added successfully!'}), 201
    return jsonify({'error': 'No item provided!'}), 400

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if 0 <= item_id < len(items):
        deleted_item = items.pop(item_id)
        return jsonify({'message': 'Item deleted successfully!', 'item': deleted_item})
    return jsonify({'error': 'Item not found!'}), 404



if __name__=="__main__":
	app.run()
