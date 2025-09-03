from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/logo/template', methods=['POST'])
def logo_template():
    return jsonify({
        "detector": "logo_template_match",
        "pass": True,
        "confidence": 0.95
    })

@app.route('/logo/clearspace', methods=['POST'])
def logo_clearspace():
    return jsonify({
        "detector": "logo_clearspace",
        "pass": False,
        "measured_ratio": 0.18
    })

@app.route('/colours/palette', methods=['POST'])
def colours_palette():
    return jsonify({
        "detector": "palette_deltaE",
        "pass": False,
        "found_colour": "#FFD700",
        "closest_allowed": "Maybank Yellow",
        "deltaE": 8.2
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
