from flask import Flask, jsonify

app = Flask(__name__)

airport_database = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EGLL": {"Name": "Heathrow Airport", "Location": "London"},
}

@app.route('/airport/<string:icao>', methods=['GET'])
def get_airport_info(icao):
    airport_info = airport_database.get(icao.upper())

    if airport_info:
        result = {"ICAO": icao.upper(), "Name": airport_info["Name"], "Location": airport_info["Location"]}
        return jsonify(result)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    print("Flask app is running. Access the airport information endpoint at http://127.0.0.1:5000/airport/EGLL")
    app.run(debug=True)
