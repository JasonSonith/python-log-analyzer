from pathlib import Path  # for file paths
import re

# Handle imports for both module and direct execution
try:
    from utils import extract_ip_address, extract_timestamp, append_suspicious_event, classify_event
except ImportError:
    from src.utils import extract_ip_address, extract_timestamp, append_suspicious_event, classify_event

# Finds all log files in the given directory


def find_log_files(log_dir, suffix=".log"):
    log_dir = Path(log_dir)
    return [file for file in log_dir.iterdir() if file.suffix == suffix]

# Extracts events from a list of log files
def extract_login_events(log_files, include=None):
    if include is not None:
        include = set(include) #include is a set of event labels to keep

    suspicious_events = []
    for log_file in log_files:
        print(f"\n--- Checking file: {log_file} ---")
        with open(log_file, "r", errors="ignore") as f:
            for line in f:
                label = classify_event(line)
                if label is None:
                    continue
                if include and label not in include:
                    continue

                ip_address = extract_ip_address(line)
                if ip_address:
                    print(f"[{label}] {line.strip()}")
                    print(f"IP Address: {ip_address}")
                else:
                    print(f"[{label}] {line.strip()}")
                    print("IP Address: Not found")

                timestamp = extract_timestamp(line)
                append_suspicious_event(suspicious_events, ip_address, timestamp, label)

    return suspicious_events
