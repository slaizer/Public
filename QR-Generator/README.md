<div align="center">

  <h1>📍 NAS-WATANIA QR Generator</h1>
  
  <p>
    <b>A simple desktop utility to convert Google Maps links into QR Codes.</b><br>
    Built with Python and PySimpleGUI.
  </p>

  <p>
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python" alt="Python" />
    </a>
    <a href="https://pysimplegui.readthedocs.io/">
      <img src="https://img.shields.io/badge/GUI-PySimpleGUI-green?style=flat" alt="PySimpleGUI" />
    </a>
    <a href="https://pypi.org/project/qrcode/">
      <img src="https://img.shields.io/badge/Library-QRCode-yellow?style=flat" alt="QR Code" />
    </a>
  </p>

</div>

---

## 📝 Overview

This application allows users to quickly paste a URL (specifically designed for Google Maps locations) and generate a high-quality QR code image. It also features a button to instantly open the generated image for printing or sharing.

## ✨ Features

* **🔗 Instant Generation:** Converts long URLs into scannable QR codes.
* **💾 Auto-Save:** Automatically saves the result as `QR.png` in the application folder.
* **📂 Quick View:** "Open QRCODE" button launches the image using the default Windows image viewer.
* **🖥️ Simple Interface:** Clean, user-friendly GUI.

---

## 🛠️ Installation & Requirements

### 1. Compatibility
* **Operating System:** Windows (Required for the `Open QRCODE` feature).
* **Python:** Python 3.x installed.

### 2. Install Dependencies
You need `PySimpleGUI` for the interface and `qrcode` (plus `pillow` for image processing). Run this command:

```bash
pip install PySimpleGUI qrcode
```




🚀 How to Use
Run the script:

```bash
python qr.py
```

Enter Link: Paste your Google Maps link (or any URL) into the input box.

Generate: Click "Generate QR code". The app will create a file named QR.png.

View: Click "Open QRCODE" to see the result immediately.

📂 Project Structure
main.py: The application script.

QR.png: The output image file (generated after running the app).





