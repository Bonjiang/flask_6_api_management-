from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/')
def home():
    """
    Home endpoint
    ---
    responses:
      200:
        description: Welcome message
    """
    return f'Hello there from Bonnie Flask API Endpoint Server'

@app.route('/hello', methods=['GET'])
def hello_get():
    """
    Hello endpoint with GET method
    ---
    parameters:
      - name: name
        in: query
        type: string
        default: World
        description: The name parameter
      - name: middlename
        in: query
        type: string
        default: no middle name provided
        description: The middle name parameter

    responses:
      200:
        description: Hello message
    """
    name = request.args.get('name', 'World')
    middlename = request.args.get('middlename', 'no middle name provided')
    nameCapital = name.upper()
    middlenameCapital = middlename.upper()
    return f'Hello {nameCapital} {middlenameCapital}!'

@app.route('/hello', methods=['POST'])
def hello_post():
    """
    Hello endpoint with POST method
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              default: World
              description: The name parameter

    responses:
      200:
        description: Hello message
    """
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    
    name = data.get('name', 'World')
    return jsonify({'message': f'Hello {name}!'})

if __name__ == '__main__':
    app.run(debug=True)
