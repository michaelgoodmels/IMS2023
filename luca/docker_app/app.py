from flask import Flask, jsonify, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify(message=f"Hello, {name}!")

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    if 'a' not in data or 'b' not in data:
        return jsonify(error="Please provide 'a' and 'b' in the JSON body."), 400
    result = data['a'] + data['b']
    return jsonify(result=result)

@app.errorhandler(404)
def not_found(error):
    return jsonify(error="Not found"), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
