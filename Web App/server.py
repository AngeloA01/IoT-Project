from flask import Flask, jsonify, render_template, send_from_directory
import read_temp_data

app = Flask(__name__)

@app.route("/")
def index():
    result = read_temp_data.get_pressure()
    result1 = jsonify(result)
    return render_template('checkmyhealth.html', result = result1)

@app.route("/mainpage")
def mainpage():
    return render_template('mainpage.html')

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response


if __name__ == "__main__":
    app.run('0.0.0.0', port=8000)