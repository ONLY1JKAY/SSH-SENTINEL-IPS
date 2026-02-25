# SSH-Sentinel: Automated Intrusion Prevention System for LInux

## Project Oveview
SSH-Setinel is a host-based Intrusion Prevention System (IPS) designed to detect, analyze and mitigate brute-force attacks on linux servers in real-time. It monitors system authentication logs in real time, identifies malicious patterns and applies risk scoring logic to suspicious IP addresses, categorize high risk threats with geographic metadata and updates the system firewall (UFW) to drop suspicious traffic.

## Problem Statement
Public facing linux servers are frequent targets of SSH brute force attacks.
Repeated failed login atempts:
* Increase attack surface
* Indicate credential stuffing attempts
* Can overwhelm logs

Traditonal tools exist (eg Fail2ban) but this project was built to:
* Deepen understanding of linux authentication flows
* Implement custom detection logic
* Practice automated mitigation techniques

## Architecture Overview
### Flow:
  * SSH login attempt occurs
  * PAM processes authentication
  * Failed attempt written to '/var/log/auth.log'
  * SSH-Sentinel-IPS parses logs
  * IP addresses aggregrated
  * Risk Score calculated
  * High risk IPs enriched via REST API(Geo + ISP metadata)
  * Critical threats automatically blocked via UFW
  * Structured logs generated


## Features
*  **Real-time Log Ingestion:** Uses persistent file pointers to monitor '.var/log/auth.log instantly without re-reading the entire file
*  **Modular Architeture:** Seperates core logic into specialized modules for geo location, risk analysis and engine orchestration 
*  **Automated Mitigation:** Automaticaly triggers 'ufw block' commands for IPs exceeding a defined threshold
*  **Geo-Intel Enrichment:** Automatically Identifies the coountry ans ISP of attackers using external API Integration.
*  **Weighted Risk Scoring:** Evaluates threats based of attempt frequency and geographic origin to minimize false positives
*  **Persistent State Tracking:** Records security events in a structured JSON for later analysis.
*  **Systemd Integration:** Runs as a background daemon with automatic restart capabilities


## Technology Stack
* **Language:** Python
*  **Security Tools:** UFW (Uncomplicated Firewall)
*  **Linux Services:** Systemd (Service Management)
*  **Libraries:** 'requests' for GEO-AP1 communication


## Installation & Setup
### 1. Source Acquisition
First, clone the repository to your local machine:
'''
git clone [https://github.com/ONLY/1JKAY/SSH-SENTINEL-IPS.git](https://github.com/ONLY1JKAY/SSH-SENTINEL-IPS.git)
cd SSH-SENTINEL-IPS

### 2. Environment Preparation
Ensure the host has 'ufw' enabled and Python 3.8+ installed. The script requires root-level socket access to manipulate the firewall tables.

### 3. Service Integration
To ensure high availability and persistence across reboots, deploy the script as a systemd unit.
Create the unit file: 'sudo nano /etc/systemd/system/sentinel.service'

### 4. Daemon Lifecycle Management
Reload the system manager configuration, enable the unit on boot and initiate the process:
'''bash
sudo systemctl daemon-reload
sudo systemctl enable sentinel.service
sudo systemctl start sentinel.service

### 5. Telemetry & Monitoring
Monitor real-time mitigation events: 'journalctl -u sentinel.service -f'
