from flask import Flask, render_template
import read_temp_data, read_humidity

app = Flask(__name__)
# @app.route("/")
# def get_temp():
#     temp = read_temp_data.get_temperature()
#     return render_template('checkmyhealth.html', result = temp)
@app.route("/")
def get_data():
    temp = read_temp_data.get_temperature()
    humidity = read_humidity.get_humidity()
    return render_template('checkmyhealth.html', temp_result=temp, hum_result=humidity)


@app.route("/mainpage")
def mainpage():
    return render_template('mainpage.html')


if __name__ == "__main__":
    app.run('0.0.0.0', port=8000)