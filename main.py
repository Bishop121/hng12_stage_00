from flask import Flask, jsonify
from datetime import datetime, timezone
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route("/", methods=["GET"])
def get_info():
    response_data = {
        "email": "obidikeemmanuel@outlook.com",  # Replace with your actual email
        "current_datetime": datetime.utcnow().replace(tzinfo=timezone.utc).isoformat(timespec='seconds').replace("+00:00", "Z"),

        "github_url": "https://github.com/Bishop121/hng12_stage_00"  # Replace with your actual repo URL
    }
    return jsonify(response_data), 200

if __name__ == "__main__":
    app.run()
