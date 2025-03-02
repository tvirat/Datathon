from flask import Flask, jsonify, request
from flask_cors import CORS
from main import perdict_if_delay, perdict_delay_prob

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<h1>hi</h1>"

@app.route("/api/delay", methods=["POST"])
def calculate_delay():
    try:
        response = request.json
        month = response["month"]
        hour = response["hour"]
        minute = response["minute"]
        day_of_week = response["day_of_week"]
        station = response["station"]
        line = response["line"]
        bound = response["bound"]
        if_delay = bool(perdict_if_delay(month, hour, minute, day_of_week, station, line, bound))
        delay_prob = perdict_delay_prob(month, hour, minute, day_of_week, station, line, bound)
        response = {
            "ifDelay": if_delay,
            "delayProb": delay_prob[1]
            }
        return jsonify(response)

    except Exception as e:
        return f"Some error occurred: {str(e)}", 500
    

if __name__ == '__main__':
    app.run(debug=True)