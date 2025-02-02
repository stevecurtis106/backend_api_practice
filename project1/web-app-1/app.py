from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def verify_params(params, function_name):
    retval = None

    if function_name == 'add' or function_name == "subtract" or function_name == "multiply":
        if 'x' not in params or 'y' not in params:
            retval = 301
        elif not isinstance(params['x'], (int, float)) or not isinstance(params['y'], (int, float)):
            retval = 302
        else:
            retval = 200
    elif function_name == 'divide':
        if 'x' not in params or 'y' not in params:
            retval = 301
        elif not isinstance(params['x'], (int, float)) or not isinstance(params['y'], (int, float)):
            retval = 302
        elif params['y'] == 0:
            retval = 303
        else:
            retval = 200

    return retval


class Add(Resource):
    def post(self):
        request_params = request.get_json()

        status_code = verify_params(request_params, 'add')

        retmap = {
            "Status Code": status_code
        }

        if status_code == 200:
            x = request_params["x"]
            y = request_params["y"]
            sum = x + y

            retmap["sum"] = sum 
        else:
            retmap["Message"] = "An error occurred. Please check your input."

        return jsonify(retmap)
    
    
class Subtract(Resource):
    def post(self):
        request_params = request.get_json()

        status_code = verify_params(request_params, 'subtract')

        retmap = {
            "Status Code": status_code
        }

        if status_code == 200:
            x = request_params["x"]
            y = request_params["y"]
            difference = x - y

            retmap["difference"] = difference
        
        else:
            retmap["Message"] = "An error occurred. Please check your input."

        return jsonify(retmap)
    

class Multiply(Resource):
    def post(self):
        request_params = request.get_json()
        status_code = verify_params(request_params, 'multiply')

        retmap = {
            "Status Code": status_code
        }

        if status_code == 200:
            x = request_params["x"]
            y = request_params["y"]
            product = x * y

            retmap["product"] = product

        else:
            retmap["Message"] = "An error occurred. Please check your input."

        return jsonify(retmap)
    

class Divide(Resource):
    def post(self):
        request_params = request.get_json()
        status_code = verify_params(request_params, 'divide')

        retmap = {
            "Status Code": status_code
        }

        if status_code == 200:
            x = request_params["x"]
            y = request_params["y"]
            quotient = x / y

            retmap["quotient"] = quotient

        elif status_code == 301 or status_code == 302:
            retmap["Message"] = "An error occurred. Please check your input."
        
        elif status_code == 303:
            retmap["Message"] = "An error occurred. Division by zero is not allowed."

        return jsonify(retmap)

    
api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
