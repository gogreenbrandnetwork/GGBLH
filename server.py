import json
from flask import Flask, request, jsonify
from tools.lookup_lottery import lookup_lottery
from tools.eligibility_check import eligibility_check
from tools.rent_stabilization import rent_stabilization
from tools.case_lookup import case_lookup, get_full_case_details, get_legal_issues, get_action_plan
from tools.motion_generator import motion_generator, generate_affidavit
from tools.deadline_tracker import deadline_tracker, track_court_dates, get_document_checklist

app = Flask(__name__)

@app.post("/run")
def run_tool():
    data = request.json
    tool = data.get("tool")
    args = data.get("arguments", {})

    # Original tools
    if tool == "lookup_lottery":
        return jsonify(lookup_lottery(**args))

    if tool == "eligibility_check":
        return jsonify(eligibility_check(**args))

    if tool == "rent_stabilization":
        return jsonify(rent_stabilization(**args))

    # New case management tools
    if tool == "case_lookup":
        return jsonify(case_lookup(**args))
    
    if tool == "get_full_case_details":
        return jsonify(get_full_case_details(**args))
    
    if tool == "get_legal_issues":
        return jsonify(get_legal_issues(**args))
    
    if tool == "get_action_plan":
        return jsonify(get_action_plan(**args))
    
    if tool == "motion_generator":
        return jsonify(motion_generator(**args))
    
    if tool == "generate_affidavit":
        return jsonify(generate_affidavit(**args))
    
    if tool == "deadline_tracker":
        return jsonify(deadline_tracker(**args))
    
    if tool == "track_court_dates":
        return jsonify(track_court_dates(**args))
    
    if tool == "get_document_checklist":
        return jsonify(get_document_checklist(**args))

    return jsonify({"error": "Unknown tool"}), 400

@app.get("/health")
def health():
    return jsonify({"status": "healthy", "version": "1.1.0"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
