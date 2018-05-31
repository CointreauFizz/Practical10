from flask import Flask, render_template

@app.route('/tempConversion')
def my_form_post():
        celsiusTemp = request.form['tempInCelsius']
        celsiusTemp = float(celsiusTemp)
        fahrenheitTemp = ((9/5) * celsiusTemp) + 32
        return str(fahrenheitTemp)

if __name__ == '__main__':
    app.run(debug=True)