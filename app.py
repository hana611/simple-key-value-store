from flask import Flask, request, jsonify

app = Flask(__name__)
store = {}

@app.route('/set', methods=['POST'])
def set_value():
    data = request.get_json(silent=True) or {}
    key = data.get('key')
    value = data.get('value')
    if not key:
        return jsonify({"error": "Key is required"}), 400
    store[key] = value
    return jsonify({"message": "Key stored successfully"}), 200

@app.route('/get/<key>', methods=['GET'])
def get_value(key):
    if key not in store:
        return jsonify({"error": "Key not found"}), 404
    return jsonify({"key": key, "value": store[key]}), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
