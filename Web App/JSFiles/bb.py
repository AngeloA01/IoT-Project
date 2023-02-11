from flask import Flask, jsonify
import read_temp_data

app = Flask(__name__)

@app.route("/")
def index():
    result = read_temp_data.run()
    return jsonify(result)

if __name__ == "__main__":
    app.run()