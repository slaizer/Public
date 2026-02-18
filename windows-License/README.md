<div align="center">

  <h1>🔑 Windows License Key Extractor</h1>
  
  <p>
    <b>A lightweight Python utility to recover your Windows Product Key.</b><br>
    Reads the encrypted key from the Registry, decodes it, and displays it in a GUI.
  </p>

  <p>
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python" alt="Python" />
    </a>
    <a href="https://pysimplegui.readthedocs.io/">
      <img src="https://img.shields.io/badge/GUI-PySimpleGUI-green?style=flat" alt="PySimpleGUI" />
    </a>
    <a href="https://www.microsoft.com/windows">
      <img src="https://img.shields.io/badge/OS-Windows_Only-0078D6?style=flat&logo=windows" alt="Windows" />
    </a>
  </p>

</div>

---

## 📝 Overview

Have you lost your Windows installation key? This tool scans the Windows Registry (`HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion`), extracts the binary `DigitalProductId`, and decodes it into a readable 25-character Product Key (e.g., `XXXXX-XXXXX-XXXXX-XXXXX-XXXXX`).

## ✨ Features

* **🛡️ Registry Access:** securely reads the `DigitalProductId` without modifying system files.
* **🔓 Smart Decoding:** Uses the Base-24 decoding algorithm to translate binary registry data into a human-readable key.
* **🖥️ Simple GUI:** No command line needed—just click "Retrieve License Key".
* **📋 Clipboard Friendly:** The output is displayed in a text box for easy copying.

---

## 🛠️ Installation & Requirements

### 1. Prerequisites
* **Operating System:** Windows (Required to access the `winreg` library).
* **Python:** Python 3.x installed.

### 2. Install Dependencies
You need `PySimpleGUI` for the interface.

```bash
pip install PySimpleGUI
```

How to Use
Run the script:

Bash
python key_extractor.py
Retrieve Key: Click the "Retrieve License Key" button.

View Result: The key will appear in the text box below.

Exit: Click Exit to close the application (includes a confirmation popup).

⚠️ Compatibility Note
Retail vs. OEM: This tool works best for Retail licenses and upgrades stored in the software registry.

BIOS Keys: If your laptop came with Windows pre-installed (OEM), the key might be stored in the motherboard's BIOS/UEFI, which requires a different method to extract.

Digital Entitlements: Newer Windows 10/11 activations linked to a Microsoft Account may not return a usable key via this method.

📄 License
This tool is for educational and personal recovery purposes.



