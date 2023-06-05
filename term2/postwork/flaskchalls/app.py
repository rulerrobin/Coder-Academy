# Your challenge is to create a calculator API. It should be able to add, subtract, multiply and divide any two integers, and return a JSON object with the operation as a string and the result as a number. Attempting to perform any operation outside of these four should return a 404 NOT FOUND error.

# /calculator/1/add/1

#     "operation": "1 plus 1",
#    "result": 2

from flask import Flask
import json

app = Flask(__name__)

@app.route('/calculator/<int:num1>/add/<int:num2>')
def add(num1, num2):
    result = {
        "operation": f"{num1} plus {num2}",
        "result": num1 + num2
    }
    return json.dumps(result)

@app.route('/calculator/<int:num1>/subtract/<int:num2>')
def subtract(num1, num2):
    result = {
        "operation": f"{num1} minus {num2}",
        "result": num1 - num2
    }
    return json.dumps(result)

@app.route('/calculator/<int:num1>/multiply/<int:num2>')
def multiply(num1, num2):
    result = {
        "operation": f"{num1} multiplied {num2}",
        "result": num1 * num2
    }
    return json.dumps(result)

@app.route('/calculator/<int:num1>/divide/<int:num2>')
def divide(num1, num2):
    result = {
        "operation": f"{num1} dvided by {num2}",
        "result": num1 / num2
    }
    return json.dumps(result)

if __name__ == '__main__':
    app.run()








# @app.route("/calculator/<int:first_number>/add/<int:second_number>")
# def add(first_number, second_number):
#     output = {
#         "operation": f"{first_number} plus {second_number}",
#         "result": first_number+second_number
#     }
#     return json.dumps(output)