#  Threat Detector and Analyzer  

## Overview  
The **Threat Detector and Analyzer** is a Python-based tool that parses system log files, detects suspicious login activity, and generates structured summaries.  
It highlights suspicious IP addresses, counts repeated events, classifies them (failed logins, invalid users, sudo failures, disconnects), and provides optional IP geolocation.  

This project demonstrates Python scripting, log parsing, and cybersecurity automation.  

---

## Features  
- Parse Linux-style log files (`/var/log/auth.log` and similar)  
- Detect events such as:  
  - Failed password attempts  
  - Invalid user logins  
  - Successful logins  
  - Sudo authentication failures  
  - Disconnection events  
- Extract IP addresses and timestamps from logs  
- Log suspicious events to a JSON file  
- Summarize IP activity with counts and color-coded risk levels  
- Optional IP geolocation lookup via `ipinfo.io`  

---

## Example Output  

### Console log detection
```
--- Checking file: sample.log ---
[FAILED_LOGIN] Failed password for invalid user admin from 192.168.1.50 port 22
IP Address: 192.168.1.50
```

### Suspicious events JSON (`suspicious_events.json`)
```json
[
    {
        "ip": "192.168.1.50",
        "timestamp": "Jan 12 14:22:33",
        "event": "FAILED_LOGIN"
    }
]
```

### Summarized IP table
```
+-----------------+---------+------------------+
| IP Address      | Count   | Location         |
+=================+=========+==================+
| 192.168.1.50    | 15      | Private IP       |
| 203.0.113.5     | 4       | Los Angeles, US  |
+-----------------+---------+------------------+
```

---

## Installation  

Clone the repository and install dependencies:  

```bash
git clone https://github.com/JasonSonith/AI-Threat-Analyzer.git
cd AI-Threat-Analyzer
pip install -r requirements.txt
```

Requirements:  
- Python 3.9+  
- colorama  
- tabulate  
- requests  

---

## Usage  

Analyze a single log file:  
```bash
python analyzer.py --logfile sample.log
```

Analyze all `.log` files in a directory (default: `tmp/logs`):  
```bash
python analyzer.py --logdir logs/
```

---

## File Structure  
- **analyzer.py** – Main entry point, handles CLI and workflow  
- **log_parser.py** – Scans log files, extracts events with regex patterns  
- **utils.py** – Regex utilities for IP, timestamps, and event classification  
- **json_logger.py** – Saves suspicious events into JSON reports  
- **ip_summary.py** – Summarizes IP activity with counts and geolocation  

---

## Skills Demonstrated  
- Python CLI scripting (`argparse`, `os`, `pathlib`)  
- Regex-based event detection  
- Structured logging with JSON  
- Data summarization with tabular CLI output  
- Use of external APIs for IP geolocation (`ipinfo.io`)  
- Color-coded CLI feedback for better readability  

