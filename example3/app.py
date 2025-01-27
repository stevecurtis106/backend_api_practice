from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/add_two_nums', methods=['POST'])
def add_two_nums():
    dataDict = request.get_json()
    x = dataDict["x"]
    y = dataDict["y"]
    z = x + y

    retJson = {
        "z": z
    }

    return jsonify(retJson), 200

if __name__ == '__main__':
    app.run()   