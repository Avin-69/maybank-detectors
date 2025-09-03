from flask import Flask, request, jsonify

app = Flask(__name__)

def handle_image_upload(detector_name, stub_confidence=0.95):
    """
    Generic handler for detectors:
    - Expects a multipart/form-data POST with field 'image'
    - Returns detector name, filename, and a stubbed confidence score
    """
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    image_file = request.files["image"]

    return jsonify({
        "detector": detector_name,
        "pass": True,                      # Stub: always passes
        "filename": image_file.filename,   # Echo filename
        "confidence": stub_confidence      # Stub confidence score
    })

@app.route("/logo/template", methods=["POST"])
def logo_template():
    return handle_image_upload("logo_template_match", 0.97)

@app.route("/logo/clearspace", methods=["POST"])
def logo_clearspace():
    return handle_image_upload("logo_clearspace", 0.92)

@app.route("/colours/palette", methods=["POST"])
def colours_palette():
    return handle_image_upload("palette_deltaE", 0.89)

# Root health check (optional)
@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "Maybank detectors API running"}), 200

if __name__ == "__main__":
    # Bind to all interfaces so Render can reach it
    app.run(host="0.0.0.0", port=5000)
