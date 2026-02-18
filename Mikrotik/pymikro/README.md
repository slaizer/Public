<div align="center">

  <h1>🛡️ MikroTik & Windows Automation Tool</h1>
  
  <p>
    <b>A powerful, menu-driven Python CLI for Network Administrators.</b><br>
    Automate MikroTik RouterOS hardening and perform essential Windows network diagnostics.
  </p>

  <p>
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Language-Python_3.x-blue?style=for-the-badge&logo=python" alt="Python" />
    </a>
    <a href="https://mikrotik.com/software">
      <img src="https://img.shields.io/badge/Platform-MikroTik_RouterOS-red?style=for-the-badge&logo=mikrotik" alt="MikroTik" />
    </a>
    <a href="https://www.microsoft.com/windows">
      <img src="https://img.shields.io/badge/OS-Windows-0078D6?style=for-the-badge&logo=windows" alt="Windows" />
    </a>
  </p>

  <h4>
    <a href="#-features">Features</a> | 
    <a href="#-installation--requirements">Installation</a> | 
    <a href="#-how-to-use">Usage</a>
  </h4>
</div>

<br>

## 🚀 Overview
This tool is designed to save time for **IT Support** and **Network Admins**. Instead of manually typing commands into a terminal or navigating complex RouterOS menus, you can secure your network and fix local IP issues with a single keystroke.

---

## ✨ Features

### 📡 1. MikroTik Automation (SSH)
*Connects securely via SSH to apply industry-standard security practices.*

| Feature | Description |
| :--- | :--- |
| **🚫 Block Port Scanners** | Automatically detects and blacklists IPs trying to scan your router. |
| **⚔️ Brute-Force Defense** | Adds firewall rules to drop repeated failed login attempts (SSH/FTP). |
| **🧹 Disable Unused Services** | Turns off risky services (Bandwidth Server, Socks, etc.) to reduce attack surface. |
| **🛡️ ICMP Security** | Advanced ping filtering to prevent floods while allowing diagnostics. |
| **🛑 DNS Guard** | Drops unauthorized DNS requests to prevent amplification attacks. |

### 💻 2. Windows Local Tools
*Instant diagnostic and maintenance utilities for your local machine.*

- **📊 Network Info:** View IP, Gateway, DNS, and MAC Address in a single, clean summary.
- **🔄 IP Refresh:** Release and Renew IP addresses automatically (fixes "No Internet" issues).
- **🧹 Cache Cleaner:** Restarts **Chrome** or **Edge** with a fresh cache (essential for web testing).

---

## 🛠️ Installation & Requirements

### Prerequisites
* **Python 3.x** installed ([Download Here](https://www.python.org/downloads/)).
* **Windows OS** (required for the local tools module).

