from flask import Flask, render_template
import read_temp_data, read_humidity, read_pressure, read_C02, read_TVOC, get_advice
import firebase_admin
from flask import Flask, Response
from flask import Flask, jsonify
from firebase_admin import credentials, db
import time



# Fetch the service account key JSON file contents
cred = credentials.Certificate('/Users/ziyadansari/Documents/Github repos/IoT-Project/Web App/embedded-lab-2-part-2-firebase-adminsdk-676w2-d21fb25bd3.json')

# Initialize the app with a custom auth variable, limiting the server's access
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://embedded-lab-2-part-2-default-rtdb.europe-west1.firebasedatabase.app/'
})

app = Flask(__name__)

@app.route("/C02_stream")
def stream_C02():
    C02 = read_C02.get_C02()
    return jsonify({"C02": C02}) 

@app.route("/TVOC_stream")
def stream_TVOC():
    TVOC = read_TVOC.get_TVOC()
    return jsonify({"TVOC": TVOC})

@app.route("/Temperature_stream")
def stream_Temperature():
    Temperature = read_temp_data.get_Temperature()
    return jsonify({"Temperature": Temperature})

@app.route("/Pressure_stream")
def stream_Pressure():
    Pressure = read_pressure.get_Pressure()
    return jsonify({"Pressure": Pressure})

@app.route("/Humidity_stream")
def stream_Humidity():
    Humidity = read_humidity.get_Humidity()
    return jsonify({"Humidity": Humidity})



@app.route("/")
def get_data():
    Temperature = read_temp_data.get_Temperature()
    Humidity = read_humidity.get_Humidity()
    Pressure = read_pressure.get_Pressure()
    Advice = get_advice.getadvice()
    TVOC = read_TVOC.get_TVOC()
    C02 = read_C02.get_C02()
    return render_template('checkmyhealth.html', Advice_result = Advice, C02_result=C02, TVOC_result=TVOC, Temperature_result=Temperature, Humidity_result=Humidity, Pressure_result=Pressure)

@app.route("/howitworks.html")
def mainpage():
    return render_template('howitworks.html')

@app.route("/checkmyhealth.html")
def secondpage():
    Temperature = read_temp_data.get_Temperature()
    Humidity = read_humidity.get_Humidity()
    Pressure = read_pressure.get_Pressure()
    TVOC = read_TVOC.get_TVOC()
    Advice = get_advice.getadvice()
    C02 = read_C02.get_C02()
    return render_template('checkmyhealth.html', Advice_result = Advice, C02_result=C02, TVOC_result=TVOC, Temperature_result=Temperature, Humidity_result=Humidity, Pressure_result=Pressure)

@app.route("/mainpage.html")
def thirdpage():
    return render_template('mainpage.html')

@app.route("/about.html")
def fourthpage():
    return render_template('about.html')

if __name__ == "__main__":
    app.run('0.0.0.0', port=8000, debug = False)