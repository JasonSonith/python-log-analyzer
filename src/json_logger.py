import json  # for logging findings to json file

def log_suspicious_events(events, output_file):
    with open(output_file, "w") as file:
        json.dump(events, file, indent=4)
    print(f"Suspicious events logged to {output_file}")
