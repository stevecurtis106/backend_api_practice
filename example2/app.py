from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_json():
    retval = {
        "name": "James",
        "age": 25,
        "location": "New York"
    }

    return jsonify(retval)

if __name__ == '__main__': 
    app.run(host="127.0.0.1", port=5000)

