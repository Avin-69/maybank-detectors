import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# --- Detector endpoints ---

@app.route('/logo/template', methods=['POST'])
def logo_template():
    # Stub response for now — replace with real OpenCV logic later
    return jsonify({
        "detector": "logo_template_match",
        "pass": True,
        "confidence": 0.95,
        "details": {
            "matched_template": "maybank_logo_master.png"
        }
    })


@app.route('/logo/clearspace', methods=['POST'])
def logo_clearspace():
    # Stub response for now — replace with real bounding box logic later
    return jsonify({
        "detector": "logo_clearspace",
        "pass": False,
        "measured_ratio": 0.18,
        "required_ratio": 0.25
    })


@app.route('/colours/palette', methods=['POST'])
def colours_palette():
    # Stub response for now — replace with real ΔE colour comparison later
    return jsonify({
        "detector": "palette_deltaE",
        "pass": False,
        "found_colour": "#FFD700",
        "closest_allowed": "Maybank Yellow",
        "deltaE": 8.2
    })


# --- Railway / Local run configuration ---
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Railway provides PORT
    app.run(host="0.0.0.0", port=port)
