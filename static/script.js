document.addEventListener("DOMContentLoaded", function () {
    document.querySelector("button").addEventListener("click", generateQR);
});

function generateQR() {
    let ssid = document.getElementById("ssid").value.trim();
    let password = document.getElementById("password").value.trim();

    if (!ssid || !password) {
        alert("Enter both SSID and Password!");
        return;
    }

    fetch("/generate_qr", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ssid: ssid, password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.qr_code) {
            let qrImage = document.getElementById("qrImage");
            qrImage.src = data.qr_code;
            qrImage.style.display = "block";
        }
    })
    .catch(error => console.error("Error generating QR:", error));
}

