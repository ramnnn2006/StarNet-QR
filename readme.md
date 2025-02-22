# WiFi QR Code Generator

## Overview
This project is a web-based WiFi QR Code Generator that allows users to enter their WiFi SSID and password to generate a QR code. Scanning the QR code makes connecting to WiFi seamless.

## Features
- **Dynamic QR Code Generation** – Enter SSID and password to generate a QR code.
- **Stylish UI** – Dark theme with a starry background and animated shooting stars.
- **Responsive Design** – Works on both mobile and desktop devices.
- **Interactive UI** – Smooth and user-friendly interface.

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Flask (Python)  
- **QR Code Generation:** `qrcode[pil]` Python library  

---

## Installation & Setup
### 1. Clone the Repository
```bash
git clone https://github.com/ramnnn2006/wifi-qr-generator.git
cd wifi-qr-generator
### 2. Install depepdancies
pip install -r requirements.txt
### 3. Run the application
python app.py
The app will be available at: ```http://127.0.0.1:5000```

