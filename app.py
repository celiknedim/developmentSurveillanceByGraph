from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/increase', methods=['POST'])
def increase_value():
    index = int(request.json['index'])  
    with open('data.json', 'r') as file:
        data = json.load(file)
    data['data'][index] += 1
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)