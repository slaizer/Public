<div align="center">

  <h1>🖥️ Windows System & Network Manager</h1>
  
  <p>
    <b>A handy GUI utility for system administration and network troubleshooting.</b><br>
    Change PC names, clear browser caches, and refresh network settings with one click.
  </p>

  <p>
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python" />
    </a>
    <a href="https://pysimplegui.readthedocs.io/">
      <img src="https://img.shields.io/badge/GUI-PySimpleGUI-green?style=for-the-badge" alt="PySimpleGUI" />
    </a>
    <a href="https://www.microsoft.com/windows">
      <img src="https://img.shields.io/badge/OS-Windows_Only-0078D6?style=for-the-badge&logo=windows" alt="Windows" />
    </a>
  </p>

</div>

---

## ⚠️ Important Warning
**This script requires Administrator Privileges to function correctly.**
* It modifies the Windows Registry.
* It executes system-level network commands.
* It forcibly closes browser processes.

---

## 🚀 Features

### 💻 System Management
* **Change PC Name:** Updates the computer's Hostname in the Registry (`SYSTEM\CurrentControlSet\Services\Tcpip\Parameters`) and **immediately restarts the computer** to apply changes.

### 🌐 Network Tools
* **IP Release & Renew:** Instantly refreshes your local IP address configuration.
* **Flush DNS:** Clears the client resolver cache to fix connection issues.
* **Check DNS:** Performs an `nslookup` on a specific domain to verify DNS propagation.

### 🧹 Browser Maintenance
* **Clear/Reset Cache:** Forcibly closes the browser and restarts it with a fresh/cleared cache directory for:
    * Google Chrome
    * Microsoft Edge
    * Mozilla Firefox

---

## 🛠️ Installation & Requirements

### 1. Prerequisites
* **Windows OS** (This script uses `winreg` and Windows CMD commands).
* **Python 3.x**.

### 2. Install Dependencies
You need the `PySimpleGUI` library for the interface.

```bash
pip install PySimpleGUI
```

💻 How to Use
Open Command Prompt or PowerShell as Administrator.

Right-click your terminal icon and select "Run as Administrator".

Run the script:

Bash```
python Pywindosapp.py
```
Operation:

To Change PC Name: Enter the new name in the input box next to the button and click Change PC Name. ⚠️ Your PC will restart immediately.

To Check DNS: Enter a domain (e.g., google.com) in the input box and click Check DNS.

Other Buttons: Click to execute the action immediately.

⚙️ How It Works (Technical)
Registry Editing: The script uses winreg to access HKEY_LOCAL_MACHINE to update the Hostname and NV Hostname.

Browser clearing: It utilizes taskkill /f /im to ensure browsers are closed before restarting them with --disk-cache-dir flags or specific arguments.

Network: It uses subprocess to call standard Windows ipconfig utilities.




