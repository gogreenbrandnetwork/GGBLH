import json
from flask import Flask, request, jsonify
from tools.lookup_lottery import lookup_lottery
from tools.eligibility_check import eligibility_check
from tools.rent_stabilization import rent_stabilization

app = Flask(__name__)

@app.post("/run")
def run_tool():
    data = request.json
    tool = data.get("tool")
    args = data.get("arguments", {})

    if tool == "lookup_lottery":
        return jsonify(lookup_lottery(**args))

    if tool == "eligibility_check":
        return jsonify(eligibility_check(**args))

    if tool == "rent_stabilization":
        return jsonify(rent_stabilization(**args))

    return jsonify({"error": "Unknown tool"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)