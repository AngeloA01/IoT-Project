from flask import Flask, render_template
import read_temp_data, read_humidity, read_pressure

app = Flask(__name__)
# @app.route("/")
# def get_temp():
#     temp = read_temp_data.get_temperature()
#     return render_template('checkmyhealth.html', result = temp)
@app.route("/")
def get_data():
    temp = read_temp_data.get_temperature()
    humidity = read_humidity.get_humidity()
    pressure = read_pressure.get_pressure()
    return render_template('checkmyhealth.html', temp_result=temp, hum_result=humidity, press_result=pressure)

@app.route("/howitworks.html")
def mainpage():
    return render_template('howitworks.html')

@app.route("/checkmyhealth.html")
def secondpage():
    return render_template('checkmyhealth.html')

@app.route("/mainpage.html")
def thirdpage():
    return render_template('mainpage.html')

@app.route("/about.html")
def fourthpage():
    return render_template('about.html')


if __name__ == "__main__":
    app.run('0.0.0.0', port=8000)