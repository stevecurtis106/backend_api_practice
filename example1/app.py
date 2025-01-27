from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/james')
def hello_james():
    return 'Hello, James!'

@app.route('/tyler')
def hello_tyler():
    return 'Hello, Tyler!'

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
