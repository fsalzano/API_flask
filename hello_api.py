from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello():
    # Get JSON data from the request
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Missing 'name' in request payload"}), 400

    # Extract the name from the payload
    name = data['name']

    # Return the greeting
    return jsonify({"message": f"Hello {name}!"})

@app.route('/api/health_check', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
