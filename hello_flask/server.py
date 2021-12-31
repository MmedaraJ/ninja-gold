from os import name
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html', name="Jay")

@app.route('/coding')
def damn():
    return '<h1>Coding Dojo</h1>'

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>')  # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "hello " + name

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + " id " + id

if __name__ == "__main__":
    app.run(debug=True)