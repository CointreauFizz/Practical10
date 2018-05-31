from flask import Flask
from flask import request
#from flask import render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    website = '''
<!DOCTYPE html>
<html>
<body>
    <h1>Converting Celcius to Farenheit! </h1>
        <h2><p>Temperature Conversion by Celine :)</a></p></h2>
        <h1><p><a href="/tempConversion">Convert Temperature Here</a></p><h1>
</body>
</html>'''
    return website

@app.route('/tempConversion')
def my_form():
    website = '''
<!DOCTYPE html>
<html>
<body>
    <h1>Temperature Convertor</h1>
    <h2>(enter a value in Celsius, and it will be converted to Fahrenheit)</h2>
    <form action="tempConversion" method="POST">
        <input type="text" name="tempInCelsius">
        <input type="submit" value="Convert">
    </form>
</body>
</html>'''
    return website

@app.route('/tempConversion', methods=['POST'])
def my_form_post():
    celsiusTemp = request.form['tempInCelsius']
    try:
        celsiusTemp = float(celsiusTemp)

        fahrenheitTemp = ((9/5) * celsiusTemp) + 32
        return str(fahrenheitTemp)
    except:
        return "That's not a number!"



if __name__ == '__main__':
    app.run()