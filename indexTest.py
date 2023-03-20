from flask import Flask, request, jsonify

app = Flask(__name__)

items = [
    {"name" : "mouse",
    "category" : "hardware",
    "price" : 299,
    "instock" : 600},

    {"name" : "keyboard",
    "category" : "hardware",
    "price" : 899,
    "instock" : 600},

    {"name" : "monitor",
    "category" : "hardware",
    "price" : 4990,
    "instock" : 600},
]

def _find_next_name(name):
    data = [x for x in items if x['name'] == name]
    return data

print(_find_next_name("Potato"))

@app.route('/item/<name>', methods=["DELETE"])
def delete_item(name: str):

    data = _find_next_name(name)
    if not data:
        return {"error": "items does not found"}, 404
    else:
        items.remove(data[0])
        return "items deleted successfully", 200

#REST API
@app.route('/item', methods=["GET"])
def get_item():
    return jsonify(items)

# GET -by name
@app.route('/item/<name>', methods=["GET"])
def get_items_name(name):
    data = _find_next_name(name)
    return jsonify(data)

@app.route('/item', methods=["POST"])
def post_items():
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    new_data = {
        "name": name,
        "category": category,
        "price": price,
        "instock":instock,
        
    }

    if (_find_next_name(name) == name):
        return {"error": "Bad Request"}, name
    else:
        items.append(new_data)
        return jsonify(items)

@app.route('/put_item/<c_name>', methods=["PUT"])
def update_item(c_name):
    # name = request.form.get('name')
    global items
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    for items in items:
        if c_name == items["name"]:
            items["category"] = int(category)
            items["price"] = int(price)
            items["instock"] = int(instock)
            return jsonify(items)

    else:
        return "Error", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)