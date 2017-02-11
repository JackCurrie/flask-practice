
from flask import Flask
from flask import request

# Refer to own namespace
app = Flask(__name__)

# The @ is a decorator function which wraps around the lower
# function and allows us to do things with it
#
@app.route('/')
def index(name="Currie"):
    name = request.args.get('name', name)
    return "Hello Jack {}!".format(name)

#
# Debug True allows us to leave server running and have any changes detected
#
#
if __name__ == '__main__':
    app.run(debug = True, port = 8000, host = '0.0.0.0')
