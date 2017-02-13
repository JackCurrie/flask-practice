from flask import Flask
from flask import render_template

# Refer to own namespace
app = Flask(__name__)

# The @ is a decorator function which wraps around the lower
# function and allows us to do things with it
# It creates a view
@app.route('/')
@app.route('/<name>')
def index(name="Currie"):
    context = {"name" : name}
    return render_template("index.html", **context)

@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    context = {"num1": num1, "num2": num2}
    return render_template("add.html", **context)

@app.route('/multiply/<int:num1>/<int:num2>')
@app.route('/multiply/<float:num1>/<float:num2>')
@app.route('/multiply/<int:num1>/<float:num2>')
@app.route('/multiply/<float:num1>/<int:num2>')
def multiply(num1, num2):
    return "{} * {} = {}".format(num1, num2, num1*num2)


# Debug True allows us to leave server running and have any changes detected
# and hosted.
if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
