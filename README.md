# SSH-Sentinel: Automated Intrusion Prevention System

## Project Oveview
SSH-Setinel is a host-based Intrusion Prevention System (IPS) designed to mitigate brute-force attacks on linux servers. It system authentication logs in real time, ientifies malicious patterns and dynamically updates the system firewall (UFW) to drop suspicious traffic.


# Features
Real-time Log Ingestion: Parses '/var/log/auth.log' for failed SSH attempts
Automated Mitigation: Automaticaly triggers 'ufw block' commands for IPs exceeding a defined threshold.
Persistent State Tracking: Records security events in a structured JSON for later analysis.
Systemd Integration: Runs as a background daemon with automatic restart capabilities


## Technology Stack
Language: Python
Security Tools: UFW (Uncomplicated Firewall)
Linux Services: Systemd (Service Management)


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
