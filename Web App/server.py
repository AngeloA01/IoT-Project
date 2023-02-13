from flask import Flask, jsonify, render_template, send_from_directory
import read_temp_data

app = Flask(__name__)

@app.route("/")
def index():
    result = read_temp_data.get_pressure()
    return render_template('checkmyhealth.html', result = result)

@app.route("/mainpage")
def mainpage():
    return render_template('mainpage.html')



if __name__ == "__main__":
    app.run('0.0.0.0', port=8000)