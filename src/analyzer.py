import argparse  # for command line arguments
import os
import json

try:
    from log_parser import find_log_files, extract_login_events
    from ip_summary import summarize_ip_counts
    from json_logger import log_suspicious_events
    from utils import extract_ip_address, extract_timestamp, append_suspicious_event
except ImportError:
    from src.log_parser import find_log_files, extract_login_events
    from src.ip_summary import summarize_ip_counts
    from src.json_logger import log_suspicious_events
    from src.utils import extract_ip_address, extract_timestamp, append_suspicious_event

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="AI Security Log Analyzer"
    )
    parser.add_argument(
        '--logfile',
        help="Path to a single log file to analyze"
    )  # for logging a single file
    parser.add_argument(
        '--logdir',
        help="Path to directory containing log files to analyze"
    )  # for logging a directory of files
    return parser.parse_args()

def main(log_dir="tmp/logs", output_file="suspicious_events.json"):
    args = parse_arguments()  # passes the logfile to the log_file variable

    # Decide whether to analyze a single log file or a directory of log files
    if args.logfile:
        if not os.path.isfile(args.logfile):
            print(
                "Error: The specified log file does not exist: "
                f"{args.logfile}"
            )
            return
        log_files = [args.logfile]  # Single file as a list
    else:
        if not os.path.isdir(log_dir):
            print(
                "Error: The specified log directory does not exist: "
                f"{log_dir}"
            )
            return
        log_files = find_log_files(log_dir)  # Finds all log files in directory

    print(
        f" Analyzing {len(log_files)} log file(s)..."
    )
    suspicious_events = extract_login_events(log_files)
    log_suspicious_events(suspicious_events, output_file)
    summarize_ip_counts(output_file)  # Call this before the file gets overwritten

if __name__ == "__main__":
    main()