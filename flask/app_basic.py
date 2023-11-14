from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/')
def home():
    return f'Hello there from Bonnie Flask API Endpoint Server'

@app.route('/hello', methods=['GET'])
def hello_get():
    name = request.args.get('name', 'World')
    middlename = request.args.get('middlename', 'no middle name provided')
    nameCapital = name.upper()
    middlenameCapital = middlename.upper()
    return f'Hello {nameCapital} {middlenameCapital}!'

@app.route('/hello', methods=['POST'])
def hello_post():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    
    name = data.get('name', 'World')
    return jsonify({'message': f'Hello {name}!'})

if __name__ == '__main__':
    app.run(debug=True)

