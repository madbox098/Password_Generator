from flask import Flask, jsonify

app = Flask(__name__)

orders = [
    {"id": 1, "user_id": 1, "product": "Laptop"},
    {"id": 2, "user_id": 2, "product": "Phone"}
]


@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = next((o for o in orders if o["id"] == order_id), None)
    if order:
        return jsonify(order)
    return jsonify({"error": "Order not found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
