# StarNet-QR
A simple and efficient WiFi QR Code Generator for seamless connectivity
## Overview  
StarNet-QR is a web-based WiFi QR Code Generator that allows users to quickly generate a QR code for their WiFi network by entering the SSID and password. Scanning the generated QR code allows instant connection without manually entering credentials.

## Features  
- **QR Code Generation** – Converts WiFi credentials into a QR code.  
- **Minimal & Fast UI** – Clean, user-friendly, and efficient.  
- **Responsive Design** – Works seamlessly on both mobile and desktop.  
- **Local Processing** – No data is stored or sent to external servers.  

## Tech Stack  
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Flask (Python)  
- **QR Code Generation:** `qrcode[pil]` Python library  

## Installation & Setup  
### Clone the Repository  
```bash
git clone https://github.com/ramnnn2006/StarNet-QR.git
cd StarNet-QR 

###     Install Dependencies
pip install -r requirements.txt
### Run the Application
python app.py
The app will be available at: http://127.0.0.1:5000


