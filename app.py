from flask import Flask, jsonify, request
from inventory import inventory
from openfoodfacts import get_product_by_barcode

app = Flask(__name__)

@app.route("/")
def home():
    return "Food Inventory API is running!"

@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify(inventory)

@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_inventory_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item)

    return jsonify({"error": "Item not found"}), 404

@app.route("/inventory", methods=["POST"])
def add_inventory_item():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    barcode = data.get("barcode")
    price = data.get("price")
    stock = data.get("stock")

    if not barcode or price is None or stock is None:
        return jsonify({
            "error": "barcode, price and stock are required"
        }), 400

    # Fetch product details from OpenFoodFacts
    product = get_product_by_barcode(barcode)

    if product is None:
        return jsonify({
            "error": "Product not found in OpenFoodFacts"
        }), 404

    new_id = max(item["id"] for item in inventory) + 1 if inventory else 1

    new_item = {
        "id": new_id,
        "barcode": barcode,
        "product_name": product["product_name"],
        "brand": product["brand"],
        "ingredients": product["ingredients"],
        "price": price,
        "stock": stock
    }

    inventory.append(new_item)

    return jsonify(new_item), 201

@app.route("/inventory/<int:item_id>", methods=["PATCH"])
def update_inventory_item(item_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    for item in inventory:
        if item["id"] == item_id:

            # Update only the fields that were sent
            if "price" in data:
                item["price"] = data["price"]

            if "stock" in data:
                item["stock"] = data["stock"]

            return jsonify(item), 200

    return jsonify({"error": "Item not found"}), 404

@app.route("/inventory/<int:item_id>", methods=["DELETE"])
def delete_inventory_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return jsonify({"message": "Item deleted successfully"}), 200

    return jsonify({"error": "Item not found"}), 404

@app.route("/search/<barcode>", methods=["GET"])
def search_product(barcode):
    product = get_product_by_barcode(barcode)

    if product:
        return jsonify(product)

    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)