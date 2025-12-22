import re  # for regex

#basic event patterns, used to label events for regex
EVENT_PATTERNS = {
    "FAILED_LOGIN": [
        r"Failed password",
        r"authentication failure",
    ],
    "INVALID_USER": [
        r"Invalid user",
    ],
    "SUCCESS_LOGIN": [
        r"Accepted password",
        r"Accepted publickey",
    ],
    "SUDO_FAILURE": [
        r"sudo: .* authentication failure",
        r"sudo: \d+ incorrect password attempts",
    ],
    "DISCONNECT": [
        r"Connection closed by",
        r"Disconnected from",
    ],
}

#classifies events based on the EVENT_PATTERNS dictionary
def classify_event(line: str):
    low = line.lower() #lowercases the line
    for label, patterns in EVENT_PATTERNS.items():
        for pat in patterns:
            if re.search(pat, low, flags=re.IGNORECASE):
                return label
    return None


def extract_ip_address(line):
    match = re.search(r"(\d{1,3}(?:\.\d{1,3}){3})", line)
    return match.group(1) if match else None

def extract_timestamp(line):
    # Extracts timestamp from a log line. Returns 'Unknown' if not found
    timestamp_match = re.match(
        r"^\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}",
        line
    )
    return timestamp_match.group(0) if timestamp_match else "Unknown"

def append_suspicious_event(events_list, ip, timestamp, event):
    events_list.append({
        "ip": ip if ip else "Unknown",
        "timestamp": timestamp,
        "event": event
    })