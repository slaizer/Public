<div align="center">

  <h1>🕵️ Taha Exe Nmap Wrapper</h1>
  
  <p>
    <b>A Python-based CLI for advanced network reconnaissance.</b><br>
    Simplify complex Nmap scans with an interactive, color-coded menu.
  </p>

  <p>
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Language-Python_3-blue?style=for-the-badge&logo=python" alt="Python" />
    </a>
    <a href="https://nmap.org/">
      <img src="https://img.shields.io/badge/Engine-Nmap-blueviolet?style=for-the-badge&logo=kalilinux" alt="Nmap" />
    </a>
    <a href="https://www.kali.org/">
      <img src="https://img.shields.io/badge/Platform-Linux%20%2F%20Kali-black?style=for-the-badge&logo=linux" alt="Linux" />
    </a>
  </p>

</div>

---

## 🚀 Overview

**Taha Exe Nmap Wrapper** automates the complexity of Nmap flags. Instead of remembering long command strings, this tool provides a structured, interactive menu to perform everything from simple host discovery to advanced stealth and zombie scans. It features color-coded output to make analyzing results easier.

---

## ⚡ Features

The tool includes **9 specialized scanning modes**:

| Mode | Description |
| :--- | :--- |
| **1. 🌐 Network Range** | Discover active hosts in a subnet (e.g., `/24`) or specific IP range. |
| **2. 🔍 Service & Version** | Detailed scan to identify open ports and the specific service versions running on them. |
| **3. 🥷 Stealth Scan** | Uses SYN packets (`-sS`) combined with OS detection and aggressive timing. |
| **4. ⚡ Fast Scan** | Rapidly scans the top 100 most common ports. |
| **5. 🧟 Zombie Scan** | (Idle Scan) Advanced blind scanning using a "zombie" host to mask your IP address. |
| **6. 🤝 TCP Connect** | Standard full 3-way handshake scan (non-stealth). |
| **7. 📡 UDP Scan** | Identifies open UDP ports (DNS, SNMP, DHCP, etc.). |
| **8. 🔗 SCTP Scan** | Scans for Stream Control Transmission Protocol (often used in telephony). |
| **9. 🎄 Xmas Scan** | Stealthy scan that sets `FIN`, `PSH`, and `URG` flags to evade simple firewalls. |

---

## 🛠️ Prerequisites & Installation

### 1. System Requirements
* **Operating System:** Linux (Kali Linux, Ubuntu, Debian recommended) or macOS.
* **Python:** Python 3.x installed.
* **Root Privileges:** Required for Stealth, OS Detection, and Xmas scans.

### 2. Install Nmap
This script relies on the Nmap binary. Install it via your package manager:

```bash
# Debian / Ubuntu / Kali
sudo apt update && sudo apt install nmap -y

# Arch Linux
sudo pacman -S nmap

# macOS (Homebrew)
brew install nmap
