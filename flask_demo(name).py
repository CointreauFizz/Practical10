from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/greet/<name>')
def greet(name="Celine"):
 return "Hello {}".format(name)


if __name__ == '__main__':
 app.run(debug=True)