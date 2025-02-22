from flask import Flask, render_template, request, jsonify
import qrcode
from io import BytesIO
import base64
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    ssid = request.json.get("ssid", "").strip()
    password = request.json.get("password", "").strip()

    if not ssid or not password:
        return jsonify({"error": "SSID and Password required"}), 400

    qr = qrcode.make(f"WIFI:S:{ssid};T:WPA;P:{password};;")  
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    qr_data = base64.b64encode(buffer.getvalue()).decode()

    return jsonify({"qr_code": f"data:image/png;base64,{qr_data}"})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 10000)) 
    app.run(host="0.0.0.0", port=port, debug=True)
