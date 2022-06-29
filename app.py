from flask import Flask, jsonify, request
import json

response = ''

app = Flask(__name__)

@app.route('/name', methods = ['GET', 'POST'])
def nameRoute():

    global response

    if(request.method == 'POST'):
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        name = request_data['name']
        response = f'{name}'
        return " "

    else:
        return jsonify({'name' : response})   

@app.route('/name2', methods = ['GET'])
def nameRoute2():

    global response

    response2 = f'Hello {response}!'

    return jsonify({'name2' : response2})
    
if __name__ == "__main__":
    app.run(debug=True)
