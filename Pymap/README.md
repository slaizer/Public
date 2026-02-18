# Taha Exe Python Nmap Wrapper

A Python-based CLI tool designed to simplify network reconnaissance using the Nmap engine. This script provides an interactive menu for various scanning techniques, from simple host discovery to advanced stealth and zombie scans, with color-coded terminal output for better readability.

## 🚀 Features

The tool provides 9 specialized scanning modes:
1. **Network Range Scanning:** Discover active hosts in a subnet (e.g., `/24`) or specific IP range.
2. **Service & Version Detection:** Detailed scan for open ports with service versioning.
3. **Stealth Scan:** SYN scanning (`-sS`) combined with OS detection and aggressive timing.
4. **Fast Scan:** Quick scan targeting the most common ports.
5. **Zombie Scan (Idle Scan):** Advanced blind scanning using an idle host to mask the scanner's IP.
6. **TCP Connect Scan:** Standard TCP handshake scan.
7. **UDP Scan:** Identification of open UDP ports.
8. **SCTP Scan:** Advanced Stream Control Transmission Protocol scanning.
9. **Xmas Scan:** Stealthy scan that sets FIN, PSH, and URG flags.

## 🛠 Prerequisites

Before running the script, ensure you have the following installed:

* **Nmap:** The script is a wrapper for the Nmap binary.
  ```bash
  sudo apt update && sudo apt install nmap -y
