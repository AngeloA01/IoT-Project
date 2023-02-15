from flask import Flask, render_template
import read_temp_data, read_humidity, read_pressure, read_C02, read_TVOC

app = Flask(__name__)
# @app.route("/")
# def get_temp():
#     temp = read_temp_data.get_temperature()
#     return render_template('checkmyhealth.html', result = temp)
@app.route("/")
def get_data():
    Temperature = read_temp_data.get_temperature()
    Humidity = read_humidity.get_humidity()
    Pressure = read_pressure.get_pressure()
    TVOC = read_TVOC.get_TVOC()
    C02 = read_C02.get_C02()
    return render_template('checkmyhealth.html', C02_result=C02,TVOC_result=TVOC, Temperature_result=Temperature, Humidity_result=Humidity, Pressure_result=Pressure)

@app.route("/howitworks.html")
def mainpage():
    return render_template('howitworks.html')

@app.route("/checkmyhealth.html")
def secondpage():
    Temperature = read_temp_data.get_temperature()
    Humidity = read_humidity.get_humidity()
    Pressure = read_pressure.get_pressure()
    TVOC = read_TVOC.get_TVOC()
    C02 = read_C02.get_C02()
    return render_template('checkmyhealth.html', C02_result=C02, TVOC_result=TVOC, Temperature_result=Temperature, Humidity_result=Humidity, Pressure_result=Pressure)

@app.route("/mainpage.html")
def thirdpage():
    return render_template('mainpage.html')

@app.route("/about.html")
def fourthpage():
    return render_template('about.html')


if __name__ == "__main__":
    app.run('0.0.0.0', port=8000)