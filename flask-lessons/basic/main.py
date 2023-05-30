from flask import Flask, request

app = Flask(__name__)

@app.route('/') # working on main page as `/` is root directory
def index(): # can be called anything but index is just convention
    return '<h3>Hello World!</h3>'
# Hook defines where route is handled
# Handler function defines what it does when it is called

@app.route('/spam')
def spam():
    person = {'name': 'John', 'age': 21}
    return person, 201 
    # if we want a specific return status place after value for return

@app.errorhandler(404) # controls what happens at response numbers
def not_found(error): # this can be named anything
    print (error)
    return {'error': str(error)}, 404

# Second segment of the URI is a parameter called 'foo'
# Flask does this:
#   1. Creates a variable called 'foo'
#   2. Set the 'foo' variable to the value in the URI in thes same position as the parameter 
#   3. Calls the handler function, passing in 'foo'

@app.route('/hello/<foo>') # gets the value of returned function 
# `<>` turns this into RESTful 
def hello(foo): 
    # foo = request.args.get('name') # args meaning argument then gets value of key if existing
    return {'message': f'Hello, {foo}!'}

@app.route('/add/<int:num1>/<int:num2>') # RESTful because using API tool 
def add(num1, num2):

    #try: # will try to do this and if there is an exception returns errors
        # x = int(request.args.get('num1')) #flask automatically makes strings
        # y = int(request.args.get('num2')) # when doing this keys need to be in or it will error as they do not exist until presented

        # y = num1
        # y = num2

        # instead of casting we can declare in route what type they should be

        return {'result': num1 + num2} 

    # except (TypeError, ValueError):
    #     return {'error': 'num1 and num2 are required and must be integers'}, 400


if __name__ == '__main__':
    app.run(debug=True) 
    # due to debug = true if there is a file change, file updates and incorporates